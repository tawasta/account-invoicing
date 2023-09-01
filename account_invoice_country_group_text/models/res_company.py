from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    invoice_report_country_text = fields.Boolean(
        string="Show country text for this company's Invoice print",
    )
