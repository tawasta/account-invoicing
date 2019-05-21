# -*- coding: utf-8 -*-
from odoo import api, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.onchange('partner_id', 'partner_invoice_id', 'company_id')
    def _onchange_partner_invoice_id(self):
        # Override onchange to use partner_invoice_id instead of partner_id

        res = super(AccountInvoice, self)._onchange_partner_id()

        transmit_method_id = False
        partner_bank_id = False
        payment_term_id = False

        if self.partner_invoice_id and self.type:
            partner = self.partner_invoice_id

            if self.type in ('out_invoice', 'out_refund'):
                payment_term_id = partner.property_payment_term_id.id

                transmit_method_id = self.transmit_method_id = \
                    partner.customer_invoice_transmit_method_id.id or False
            else:
                bank_ids = partner.commercial_partner_id.bank_ids
                partner_bank_id = bank_ids[0].id if bank_ids else False

                payment_term_id = partner.property_supplier_payment_term_id.id
                transmit_method_id = self.transmit_method_id = \
                    partner.supplier_invoice_transmit_method_id.id or False

        self.payment_term_id = payment_term_id
        self.transmit_method_id = transmit_method_id
        self.partner_bank_id = partner_bank_id

        return res

    @api.model
    def create(self, vals):
        if vals.get('type') and vals.get('partner_invoice_id'):

            partner = self.env['res.partner'].browse(
                vals['partner_invoice_id']
            )

            if vals['type'] in ('out_invoice', 'out_refund'):
                if 'transmit_method_id' not in vals:
                    vals['transmit_method_id'] = \
                        partner.customer_invoice_transmit_method_id.id or False
                if 'payment_term_id' not in vals:
                    vals['payment_term_id'] = \
                        partner.customer_invoice_transmit_method_id.id or False
            else:
                if 'transmit_method_id' not in vals:
                    vals['transmit_method_id'] =\
                        partner.supplier_invoice_transmit_method_id.id or False

                if 'partner_bank_id' not in vals:
                    bank_ids = partner.commercial_partner_id.bank_ids
                    partner_bank_id = bank_ids[0].id if bank_ids else False

                    vals['partner_bank_id'] = partner_bank_id

                if 'payment_term_id' not in vals:
                    vals['payment_term_id'] = \
                        partner.supplier_invoice_transmit_method_id.id or False

        return super(AccountInvoice, self).create(vals)
