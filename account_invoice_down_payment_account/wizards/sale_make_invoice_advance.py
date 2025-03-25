from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoices(self, sale_orders):
        invoice = super()._create_invoices(sale_orders)

        product = self.product_id or self._default_product_id()
        new_account = product._get_product_accounts().get("receivable")

        # If partner-spesific
        if new_account:
            for line in invoice.line_ids:
                if new_account and line.account_id.account_type in (
                    "asset_receivable",
                    "liability_payable",
                ):
                    line.account_id = new_account

        return invoice
