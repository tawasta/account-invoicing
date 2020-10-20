from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    product_unit_count_category_id = fields.Many2one(
        string="Product unit count category",
        comodel_name="product.category",
        help="Leave empty to count any products",
    )
