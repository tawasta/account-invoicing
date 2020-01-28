from odoo import api, models


class AccountInvoiceLine(models.Model):

    _inherit = "account.invoice.line"

    @api.depends(
        "product_id", "purchase_price", "quantity", "price_unit", "price_subtotal"
    )
    def _product_margin(self):

        super(AccountInvoiceLine, self)._product_margin()

        for line in self:
            if line.product_id.margin_ignore:
                line.margin = 0
