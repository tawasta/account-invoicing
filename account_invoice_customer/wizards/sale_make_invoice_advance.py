from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        vals = super()._prepare_invoice_values(order, name, amount, so_line)
        vals["partner_customer_id"] = order.partner_id.id

        return vals
