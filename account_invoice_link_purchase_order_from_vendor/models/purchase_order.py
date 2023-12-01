from odoo import fields, models


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    bill_ids = fields.Many2many(
        "account.move",
        "bill_ids_purchase_orders_rel",
        "purchase_order",
        "bill_id",
        "Linked bills",
        copy=False,
    )
