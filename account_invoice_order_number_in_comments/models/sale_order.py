# -*- coding: utf-8 -*-
from odoo import models, api, _


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _prepare_invoice(self):
        # Handling for when invoicing the invoiceable lines
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()

        if not invoice_vals['comment']:
            invoice_vals['comment'] = ''

        invoice_vals['comment'] += \
            u'\n%s: %s' % (_('Our Order Reference'), self.name)

        return invoice_vals
