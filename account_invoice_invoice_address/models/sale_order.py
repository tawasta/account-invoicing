# -*- coding: utf-8 -*-
from odoo import api, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _prepare_invoice(self):
        # Handling for when invoicing the invoiceable lines
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['partner_id'] = self.partner_id.id
        invoice_vals['partner_invoice_id'] = self.partner_invoice_id.id

        return invoice_vals
