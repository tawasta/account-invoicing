from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoice(self, order, so_line, amount):
        res = super()._create_invoice(order, so_line, amount)

        product = self.product_id or self._default_product_id()
        new_account = product._get_product_accounts().get("receivable")

        # If partner-spesific
        if new_account:
            for line in res.line_ids:
                if new_account and line.account_id.user_type_id.type in (
                    "receivable",
                    "payable",
                ):
                    line.account_id = new_account

        return res
