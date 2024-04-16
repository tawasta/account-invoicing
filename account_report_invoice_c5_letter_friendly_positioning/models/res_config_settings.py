from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    account_report_invoice_c5_vertical_offset = fields.Integer(
        string="Invoice Report: C5 Letter Vertical Offset (px)",
        help="Adjust as needed to get the print's address to align with the "
        "C5 letter's window.",
        related="company_id.account_report_invoice_c5_vertical_offset",
        readonly=False,
        store=True,
    )
