from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends("line_ids.sale_line_ids.order_id")
    def _compute_delivery_date(self):
        """The behaviour of Delivery Date computation is completely disables
        with this change."""
        pass
