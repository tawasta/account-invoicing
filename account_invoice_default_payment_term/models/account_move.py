from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends("partner_id")
    def _compute_invoice_payment_term_id(self):
        super()._compute_invoice_payment_term_id()

        for move in self:
            default_payment_term = move.company_id.invoice_payment_term

            if (
                not move.invoice_payment_term_id
                and default_payment_term
                and move.partner_id
            ):
                move.invoice_payment_term_id = default_payment_term
