from odoo import fields, models


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    linked_account_move_id = fields.Many2one("account.move", string="Linked invoice")
