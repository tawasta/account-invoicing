from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoices(self, sale_orders):
        invoice = super()._create_invoices(sale_orders)

        product = self.product_id or self._compute_product_id()

        if product:
            new_account = product._get_product_accounts().get("receivable")

            # If partner-spesific
            if new_account and self.has_down_payments:
                for line in invoice.line_ids:
                    if new_account and line.account_id.account_type in (
                        "asset_receivable",
                        "liability_payable",
                    ):
                        line.account_id = new_account

        return invoice
