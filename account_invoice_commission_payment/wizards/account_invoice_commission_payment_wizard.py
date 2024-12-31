import logging
import time

from odoo import _, fields, models
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class AccountInvoiceCommissionPaymentWizard(models.TransientModel):
    _name = "account.invoice.commission.payment.wizard"
    _description = "Create commission payments from invoices"

    payment_date = fields.Date(
        string="Payment date", required="True", default=fields.Date.today()
    )
    commission_method = fields.Selection(
        [("cost", "Cost price")],
        string="Commission method",
        default="cost",
        required=True,
    )
    commission_partner = fields.Selection(
        [("product_owner", "Product owner")],
        string="Commission partner",
        default="product_owner",
        required=True,
    )
    communication = fields.Char(
        string="Communication",
        default=lambda self: self._default_communication(),
    )
    add_zero_sum_lines = fields.Boolean(
        string="Add zero-sum invoice lines",
        help="If unselected, zero-sum invoice lines are "
        "marked as commissioned and not added to the payment",
        default=False,
    )

    def _default_communication(self):
        return self.env.user.company_id.commission_communication

    def action_create_commission_payments(self):
        invoice_ids = self.env["account.move"].browse(self._context.get("active_ids"))

        self.create_commission_payments(invoice_ids)

    def create_commission_payments(self, invoice_ids):
        account_payments = self.env["account.payment"]

        for invoice in invoice_ids:
            account_payments |= self.create_commission_payment(invoice)

        account_payments.action_compute_commission_amount()

    def create_commission_payment(self, invoice):
        time1 = time.process_time()

        if invoice.payment_state != "paid":
            raise UserError(
                _(
                    "You can't make payment from an invoice that is not paid: '{}'"
                ).format(invoice.name)
            )

        if invoice.move_type != "out_invoice":
            raise UserError(
                _(
                    "You can only make payments from customer invoices. '{}' is not a customer invoice"
                ).format(invoice.name)
            )

        if invoice.refund_invoice_ids:
            raise UserError(
                _("Invoice '{}' has been refunded and can't be commissioned").format(
                    invoice.name
                )
            )

        if invoice.amount_total_signed == 0 and not self.add_zero_sum_lines:
            # Skip adding zero-sum invoices to payments
            invoice.commission_paid = True
            invoice.invoice_line_ids.write({"commission_paid": True})
            return

        journal = self.env["account.journal"].search(
            [
                ("type", "in", ("bank", "cash")),
                ("company_id", "=", invoice.company_id.id),
                ("currency_id", "in", [invoice.currency_id.id, False]),
            ],
            limit=1,
        )

        if not journal:
            raise ValidationError(
                _("Could not find a payment journal for '{}'").format(invoice.name)
            )

        partner_lines = self.gather_partner_lines(invoice)
        payments = self.generate_payment_data(partner_lines, journal, invoice)

        payment_records = self.env["account.payment"]

        for payment in payments:
            for line in partner_lines[payment.partner_id]:
                select_query = """
                    UPDATE account_move_line SET commission_payment_id = {}, commission_paid = 't' WHERE id = {}
                """.format(
                    payment.id,
                    line.id,
                )
                self.env.cr.execute(select_query)

            payment_records |= payment

        invoice._compute_commission_paid()

        time2 = time.process_time()
        _logger.info(
            "Processed time to create comission payments: {}".format(time2 - time1)
        )

        return payment_records

    def gather_partner_lines(self, invoice):
        partner_lines = {}

        for line in sorted(invoice.invoice_line_ids, key=lambda mline: mline.id):
            if line.price_total == 0 and not self.add_zero_sum_lines:
                _logger.info("Skipping a zero sum line")
                line.commission_paid = True
                continue

            if line.commission_payment_id:
                # Commission is already made
                _logger.info(
                    _("Commission is already paid for move line {}").format(line.id)
                )
                continue

            partner_id = self.get_commission_partner(line)
            if not partner_id:
                _logger.warning(
                    _("Partner could not be determined for '{}'").format(line.name)
                )
                # No commission partner. Mark as commissioned
                line.commission_paid = True
                continue

            if partner_id not in partner_lines:
                partner_lines[partner_id] = []

            partner_lines[partner_id].append(line)

        return partner_lines

    def generate_payment_data(self, partner_lines, journal, invoice):
        account_payment = self.env["account.payment"]
        payment_method = self.env.ref("account.account_payment_method_manual_out")

        for partner_id, lines in partner_lines.items():
            partner_bank_id = partner_id.bank_ids and partner_id.bank_ids[0]

            if not partner_bank_id:
                raise ValidationError(
                    _("Bank account could not be determined for '{}'").format(
                        partner_id.name
                    )
                )

            payment_date = self.payment_date.isoformat()

            payment = account_payment.search(
                [
                    ("state", "=", "draft"),
                    ("partner_id", "=", partner_id.id),
                    ("payment_type", "=", "outbound"),
                    ("partner_type", "=", "supplier"),
                    ("currency_id", "=", invoice.currency_id.id),
                    ("journal_id", "=", journal.id),
                    ("partner_bank_id", "=", partner_bank_id.id),
                    ("date", "=", payment_date),
                    ("commission_method", "=", self.commission_method),
                ],
                limit=1,
            )

            if not payment:
                # Create a new payment
                payment_values = {
                    "payment_type": "outbound",
                    "partner_type": "supplier",
                    "partner_id": partner_id.id,
                    "currency_id": invoice.currency_id.id,
                    "journal_id": journal.id,
                    "payment_method_id": payment_method.id,
                    "partner_bank_id": partner_bank_id.id,
                    "date": payment_date,
                    "ref": self.communication,
                    "commission_method": self.commission_method,
                }
                payment = account_payment.with_context(active_ids=False).create(
                    payment_values
                )

            yield payment

    def get_commission_partner(self, invoice_line):
        partner_id = False

        if self.commission_partner == "product_owner":
            partner_id = invoice_line.product_id.company_id.partner_id

        return partner_id
