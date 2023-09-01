from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    invoice_report_country_text = fields.Boolean(
        related="company_id.invoice_report_country_text",
        readonly=False,
        store=True,
    )
