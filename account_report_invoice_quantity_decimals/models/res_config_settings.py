from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    invoice_report_decimal_precision = fields.Integer(
        related="company_id.invoice_report_decimal_precision",
        readonly=False,
        store=True,
    )
