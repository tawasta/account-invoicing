from odoo import fields, models


class AccountMoveLine(models.Model):

    _inherit = "account.move.line"

    purchase_line_qty_received = fields.Float(related="purchase_line_id.qty_received")
    purchase_line_qty_invoiced = fields.Float(related="purchase_line_id.qty_to_invoice")
