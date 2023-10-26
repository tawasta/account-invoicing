from odoo import models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()

        invoice_vals["partner_customer_id"] = self.partner_id.id

        return invoice_vals
