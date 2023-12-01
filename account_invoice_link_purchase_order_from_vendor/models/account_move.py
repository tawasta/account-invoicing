from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    purchase_orders = fields.Many2many(
        "purchase.order",
        "bill_ids_purchase_orders_rel",
        "bill_id",
        "purchase_order",
        "Purchase orders",
        copy=False,
    )
