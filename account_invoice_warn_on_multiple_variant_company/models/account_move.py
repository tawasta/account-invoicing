from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    multiple_variant_companies_on_lines = fields.Boolean(
        string="Lines' Product Variants Contain More Than One Company",
        compute="_compute_multiple_variant_fields",
        store=False,
    )

    def _compute_multiple_variant_fields(self):
        """
        Iterate invoice lines' products and check how many different variant companies
        there are.
        """
        for move in self:

            variant_companies = {
                line.product_id.variant_company_id.id for line in move.invoice_line_ids
            }

            move.multiple_variant_companies_on_lines = len(variant_companies) > 1
