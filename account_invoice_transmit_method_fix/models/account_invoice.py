# -*- coding: utf-8 -*-
from odoo import models, api


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.model
    def create(self, vals):
        if ('transmit_method_id' not in vals and vals.get('type') and
                vals.get('partner_id')):

            partner = self.env['res.partner'].browse(vals['partner_id'])
            if vals['type'] in ('out_invoice', 'out_refund'):
                vals['transmit_method_code'] =\
                    partner.customer_invoice_transmit_method_id.code or False
            else:
                vals['transmit_method_code'] =\
                    partner.supplier_invoice_transmit_method_id.code or False

        return super(AccountInvoice, self).create(vals)
