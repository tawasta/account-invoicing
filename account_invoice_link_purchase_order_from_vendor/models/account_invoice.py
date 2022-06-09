from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    purchase_orders = fields.Many2many(
        string="Purchase orders",
        comodel_name="purchase.order",
        copy=False,
    )
