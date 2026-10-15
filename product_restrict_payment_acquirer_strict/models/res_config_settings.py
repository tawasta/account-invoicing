from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    product_acquirer_restriction_mode = fields.Selection(
        selection_add=[("all_strict", "All Products (strict)")],
        ondelete={"all_strict": "set null"},
    )
