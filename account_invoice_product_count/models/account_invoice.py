from odoo import fields, models

from odoo.addons import decimal_precision as dp


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    product_unit_count = fields.Float(
        string="Units count",
        digits=dp.get_precision("Product Unit of Measure"),
        compute="_compute_product_unit_count",
    )

    def _compute_product_unit_count(self):
        product_category = self.env["product.category"]
        uom_unit = self.env.ref("uom.product_uom_unit")
        uom_unit_category = uom_unit.category_id
        product_count = 0

        for record in self:
            main_category = record.company_id.product_unit_count_category_id.id

            if main_category:
                all_categories = product_category.search(
                    [("id", "child_of", main_category)]
                )
            else:
                all_categories = product_category.search([])

            for ail in record.invoice_line_ids:
                if (
                    ail.product_id
                    and ail.product_id.categ_id in all_categories
                    and ail.product_id.uom_id.category_id == uom_unit_category
                ):
                    product_count += ail.uom_id._compute_quantity(
                        ail.quantity, uom_unit
                    )

            record.product_unit_count = product_count
