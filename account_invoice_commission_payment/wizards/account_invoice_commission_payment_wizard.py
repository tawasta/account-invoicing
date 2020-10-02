from odoo import api, models, fields, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


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

    @api.multi
    def action_create_commission_payments(self):
        invoice_ids = self.env["account.invoice"].browse(
            self._context.get("active_ids")
        )

        account_payment = self.env["account.payment"]
        payment_method = self.env.ref("account.account_payment_method_manual_out")

        for invoice in invoice_ids:
            if invoice.state != "paid":
                raise UserError(
                    _(
                        "You can't make payment from invoice that is not paid: '{}'"
                    ).format(invoice.number)
                )

            if invoice.commission_payment_id:
                raise UserError(
                    _("Commission payment is already created for {}").format(
                        invoice.name
                    )
                )

            # Decide the cost for the payment
            amount = 0
            if self.commission_method == "cost":
                amount = invoice.invoice_line_ids.mapped("product_id.standard_price")[0]

            partner_id = False
            if self.commission_partner == "product_owner":
                partner_id = invoice.invoice_line_ids.mapped(
                    "product_id.company_id.partner_id"
                )

                if len(partner_id) > 1:
                    raise ValidationError(
                        _("Invoice lines can't have products from different owners")
                    )

            journal = self.env["account.journal"].search(
                [
                    ("type", "in", ("bank", "cash")),
                    ("company_id", "=", invoice.company_id.id),
                    ("currency_id", "in", [invoice.currency_id.id, False]),
                ],
                limit=1,
            )

            partner_bank_account_id = partner_id.bank_ids and partner_id.bank_ids[0]

            if not partner_id:
                raise ValidationError(
                    _("Partner could not be determined for '{}'").format(invoice.name)
                )

            if not journal:
                raise ValidationError(
                    _("Could not find a payment journal for for '{}'").format(
                        invoice.name
                    )
                )

            if not partner_bank_account_id:
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
                    ("partner_bank_account_id", "=", partner_bank_account_id.id),
                    ("payment_date", "=", payment_date),
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
                    "currency_id": invoice.currency_id.id,
                    "journal_id": journal.id,
                    "payment_method_id": payment_method.id,
                    "partner_bank_account_id": partner_bank_account_id.id,
                    "payment_date": payment_date,
                    "communication": _("Commission"),
                }
                payment = account_payment.with_context(active_ids=False).create(
                    payment_values
                )

            invoice.commission_payment_id = payment.id
            invoice.commission_paid = True
