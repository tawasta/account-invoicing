from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    account_move_confirmation_partner_address_required = fields.Boolean(
        string="Invoice Confirmation: Partner Address Required",
        config_parameter="account_move_confirmation.partner_address_required",
        default=False,
    )

    account_move_confirmation_partner_email_required = fields.Boolean(
        string="Invoice Confirmation: Partner E-mail Required",
        config_parameter="account_move_confirmation.partner_email_required",
        default=False,
    )

    account_move_confirmation_partner_shipping_address_required = fields.Boolean(
        string="Invoice Confirmation: Shipping Partner Address Required",
        config_parameter="account_move_confirmation.partner_shipping_address_required",
        default=False,
    )
