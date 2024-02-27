from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    payment_link = fields.Char(
        string="Payment Link",
        copy=False,
        help="Payment link to be sent to the customer.",
    )

    def action_invoice_sent(self):
        """
        Trigger the creation of the payment link when user clicks Send & Print
        for the invoice, so it is ready to be used in the e-mail template.
        """
        self.ensure_one()

        payment_link_wizard = self.env["payment.link.wizard"]

        temp_wizard = payment_link_wizard.create(
            {
                "res_model": "account.move",
                "res_id": self.id,
                "amount": self.amount_total,
                "partner_id": self.partner_id.id,
                "currency_id": self.currency_id.id,
                "description": self.payment_reference,
            }
        )

        temp_wizard._compute_values()
        self.payment_link = temp_wizard.link

        return super().action_invoice_sent()
