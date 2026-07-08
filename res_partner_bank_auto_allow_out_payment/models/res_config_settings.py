from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    auto_allow_out_payment = fields.Boolean(
        string="Automatically make bank accounts trusted",
        config_parameter="res_partner_bank_auto_allow_out_payment.auto_allow_out_payment",
        default=False,
    )
