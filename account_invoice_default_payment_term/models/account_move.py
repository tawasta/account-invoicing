from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends("partner_id")
    def _compute_invoice_payment_term_id(self):
        default_payment_term_id = int(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("account_invoice_default_payment_term.default_term")
        )
        default_payment_term = self.env["account.payment.term"].browse(
            default_payment_term_id
        )

        super()._compute_invoice_payment_term_id()

        for move in self:
            if (
                not move.invoice_payment_term_id
                and default_payment_term
                and move.partner_id
            ):
                move.invoice_payment_term_id = default_payment_term
