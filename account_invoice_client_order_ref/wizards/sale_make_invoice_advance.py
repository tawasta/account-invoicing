# -*- coding: utf-8 -*-
from odoo import api, models


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        # Handling for when invoicing a down payment
        invoice = super(SaleAdvancePaymentInv, self).\
            _create_invoice(order, so_line, amount)
        if order.client_order_ref:
            invoice.client_order_ref = order.client_order_ref

        return invoice
