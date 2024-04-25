from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_invoice(self):
        res = super()._prepare_invoice()

        # Remove default bank account
        res.pop("partner_bank_id")

        return res
