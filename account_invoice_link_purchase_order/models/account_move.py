from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    purchase_order_ids = fields.Many2many(
        string="Related purchase orders",
        comodel_name="purchase.order",
        domain=[("state", "in", ["purchase", "done"])],
    )
