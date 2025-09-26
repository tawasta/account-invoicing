from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    show_edit_delivery_date = fields.Boolean(
        compute=lambda self: self._compute_show_edit_delivery_date()
    )

    @api.depends("delivery_date")
    def _compute_show_edit_delivery_date(self):
        for move in self:
            move.show_edit_delivery_date = move.is_sale_document()
