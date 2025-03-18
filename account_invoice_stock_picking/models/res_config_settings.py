from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_account_invoice_report_pickings = fields.Boolean(
        string="Show pickings on invoice print",
        implied_group="account_invoice_stock_picking.group_account_invoice_report_pickings",
    )
