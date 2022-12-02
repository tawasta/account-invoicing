from odoo import models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    def _prepare_invoice(self):
        """Set an invoice's warranty as True if SO has a warranty"""
        invoice_vals = super(SaleOrder, self)._prepare_invoice()

        if self.warranty:
            invoice_vals["warranty"] = True

        return invoice_vals
