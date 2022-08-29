from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    hide_invoice_name = fields.Boolean(
        string="Hide invoice name",
        related="company_id.hide_invoice_name",
        readonly=False,
    )
