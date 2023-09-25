from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    purchase_orders = fields.Many2many(
        string="Purchase orders",
        comodel_name="purchase.order",
        copy=False,
    )
