from odoo import api, models


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        current_invoices = order.invoice_ids
        is_first = True
        invoice = super(SaleAdvancePaymentInv, self)._create_invoice(
            order, so_line, amount
        )
        if self.advance_payment_method in ('percentage', 'fixed'):
            for i in current_invoices:
                if i.stock_picking_ids:
                    is_first = False

            if is_first:
                for picking in order.picking_ids:
                    picking.sudo().write({'priority': '0'})
            for pick in order.picking_ids:
                invoice.sudo().write({"stock_picking_ids": [(4, pick.id)]})

        return invoice
