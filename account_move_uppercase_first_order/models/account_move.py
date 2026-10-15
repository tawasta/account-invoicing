from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"
    _order = "name_sort asc, id desc"

    name_sort = fields.Char(
        compute="_compute_name_sort",
        store=True,
        index=True,
    )

    @api.depends("name")
    def _compute_name_sort(self):
        for rec in self:
            rec.name_sort = (rec.name or "").lower()
