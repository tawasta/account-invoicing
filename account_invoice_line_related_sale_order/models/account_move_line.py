from odoo import fields, models


class AccountMoveLine(models.Model):

    _inherit = "account.move.line"

    sale_order_id = fields.Many2one("sale.order", related="sale_line_ids.order_id")
