from odoo import api, models


class AccountMoveLine(models.Model):

    _inherit = "account.move.line"

    @api.depends("purchase_price", "price_subtotal", "move_id.move_type", "quantity")
    def _compute_margin(self):

        super()._compute_margin()

        for line in self:
            if line.product_id.margin_ignore:
                line.margin = 0
                line.margin_signed = 0
                line.margin_percent = 0
