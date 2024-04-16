from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    account_report_invoice_c5_vertical_offset = fields.Integer(
        string="Invoice Report: C5 Letter Vertical Offset (px)",
        help="Adjust as needed to get the print's address to align with the "
        "C5 letter's window.",
    )
