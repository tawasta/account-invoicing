from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    invoice_payment_term = fields.Many2one(
        comodel_name="account.payment.term",
        string="Default Payment term",
        related="company_id.invoice_payment_term",
        readonly=False,
    )
