import logging
from odoo import models, fields, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

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

    def _default_communication(self):
        return self.env.user.company_id.commission_communication

    def action_create_commission_payments(self):
        invoice_ids = self.env["account.move"].browse(self._context.get("active_ids"))

        account_payment = self.env["account.payment"]
        payment_method = self.env.ref("account.account_payment_method_manual_out")

        for invoice in invoice_ids:
            if invoice.payment_state != "paid":
                raise UserError(
                    _(
                        "You can't make payment from invoice that is not paid: '{}'"
                    ).format(invoice.number)
                )

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
                    _("Could not find a payment journal for for '{}'").format(
                        invoice.name
                    )
                )

            for line in invoice.invoice_line_ids:
                if line.commission_payment_id:
                    # Commission is already made
                    continue

                # Decide the cost for the payment
                amount = 0
                if self.commission_method == "cost":
                    amount = line.purchase_price

                partner_id = False
                if self.commission_partner == "product_owner":
                    partner_id = line.product_id.company_id.partner_id

                if not partner_id:
                    _logger.warning(
                        _("Partner could not be determined for '{}'").format(line.name)
                    )
                    # No commission partner. Mark as commissioned
                    line.commission_paid = True

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
                        ("currency_id", "=", line.currency_id.id),
                        ("journal_id", "=", journal.id),
                        ("partner_bank_id", "=", partner_bank_id.id),
                        ("date", "=", payment_date),
                    ],
                    limit=1,
                )

                if payment:
                    # Just update the amount
                    payment.amount = payment.amount + amount
                else:
                    # Create a new payment
                    payment_values = {
                        "payment_type": "outbound",
                        "partner_type": "supplier",
                        "partner_id": partner_id.id,
                        "amount": amount,
                        "currency_id": line.currency_id.id,
                        "journal_id": journal.id,
                        "payment_method_id": payment_method.id,
                        "partner_bank_id": partner_bank_id.id,
                        "date": payment_date,
                        "ref": self.communication,
                    }
                    payment = account_payment.with_context(active_ids=False).create(
                        payment_values
                    )

                line.commission_payment_id = payment.id
                line.commission_paid = True

            if False not in invoice.invoice_line_ids.mapped("commission_paid"):
                # All lines are has a commission payment (or are marked as paid)
                invoice.commission_paid = True
