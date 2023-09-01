from odoo import fields, models


class BaseDocumentLayout(models.TransientModel):

    _inherit = "base.document.layout"

    invoice_report_country_text = fields.Boolean(
        related="company_id.invoice_report_country_text", readonly=True
    )
