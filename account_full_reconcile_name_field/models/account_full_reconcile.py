from odoo import fields, models


class AccountFullReconcile(models.Model):
    _inherit = "account.full.reconcile"

    name = fields.Char(
        string="Number",
        copy=False,
        default=lambda self: self.env["ir.sequence"].next_by_code("account.reconcile"),
    )
