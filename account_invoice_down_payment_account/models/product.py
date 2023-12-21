from odoo import fields, models


class Product(models.Model):

    _inherit = "product.template"

    property_account_receivable_id = fields.Many2one(
        "account.account",
        company_dependent=True,
        string="Receivable Account",
        domain="[('internal_type', '=', 'receivable'),"
        "('deprecated', '=', False),"
        "('company_id', '=', current_company_id)]",
    )

    def _get_product_accounts(self):
        res = super()._get_product_accounts()

        res["receivable"] = self.property_account_receivable_id

        return res
