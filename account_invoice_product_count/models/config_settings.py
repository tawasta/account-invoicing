from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    product_unit_count_category_id = fields.Many2one(
        related="company_id.product_unit_count_category_id", readonly=False,
    )
