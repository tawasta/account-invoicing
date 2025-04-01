from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoices(self, sale_orders):
        # Handling for when invoicing a down payment
        invoices = super()._create_invoices(sale_orders)

        for invoice in invoices:
            order = sale_orders.filtered(lambda so: so.id == invoice.invoice_origin)
            if order:
                invoice.notice_period = (
                    order.partner_id.notice_period or order.company_id.notice_period
                )

        return invoices
