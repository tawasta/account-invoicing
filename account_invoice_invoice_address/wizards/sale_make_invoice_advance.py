# -*- coding: utf-8 -*-
from odoo import api, models


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        # Handling for when invoicing a down payment
        invoice = super(SaleAdvancePaymentInv, self).\
            _create_invoice(order, so_line, amount)
        invoice.partner_id = order.partner_id.id
        invoice.partner_invoice_id = order.partner_invoice_id.id
        return invoice
