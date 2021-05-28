from odoo import api, models


class AccountInvoiceLine(models.Model):

    _inherit = "account.invoice.line"

    @api.depends("purchase_price", "price_subtotal")
    def _compute_margin(self):

        super(AccountInvoiceLine, self)._compute_margin()

        for line in self:
            if line.product_id.margin_ignore:
                line.margin = 0
                line.margin_signed = 0
                line.margin_percent = 0
