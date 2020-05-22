from odoo import fields, models


class AccountConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    notice_period = fields.Integer(
        string="Notice period (days)",
        related="company_id.notice_period",
        help="Default notice period (days) for new customers and invoices",
        readonly=False,
    )
