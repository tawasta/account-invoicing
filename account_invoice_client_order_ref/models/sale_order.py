# -*- coding: utf-8 -*-
from odoo import models, api


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _prepare_invoice(self):
        # Handling for when invoicing the invoiceable lines
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['client_order_ref'] = self.client_order_ref

        return invoice_vals
