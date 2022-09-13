from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    invoice_report_decimal_precision = fields.Integer(
        string="Product quantity's Decimal precision on Invoice print",
        help="Choose the number of decimal's shown on product quantities",
    )
