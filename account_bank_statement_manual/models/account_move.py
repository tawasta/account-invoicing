from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends("move_type")
    def _compute_invoice_filter_type_domain(self):
        res = super()._compute_invoice_filter_type_domain()
        return res
