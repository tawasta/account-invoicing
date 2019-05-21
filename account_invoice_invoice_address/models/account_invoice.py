# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    partner_invoice_id = fields.Many2one(
        comodel_name='res.partner',
        string='Invoicing address',
    )

    def _get_refund_common_fields(self):
        res = super(AccountInvoice, self)._get_refund_common_fields()

        res.append('partner_invoice_id')

        return res

    @api.onchange('partner_id')
    def onchange_partner_id_update_partner_invoice_id(self):
        for record in self:
            invoice_addresses = record.partner_id.child_ids.filtered(
                lambda r: r.type == 'invoice'
            )

            record.partner_invoice_id = invoice_addresses \
                and invoice_addresses[0] \
                or record.partner_id

    @api.model
    def create(self, vals):
        # Force using partner_invoice_id
        if not vals.get('partner_invoice_id'):
            vals['partner_invoice_id'] = vals.get('partner_id')

        return super(AccountInvoice, self).create(vals)

    @api.multi
    def write(self, vals):
        for record in self:
            # Trying to set invoice address as False
            if 'partner_invoice_id' in vals \
                    and not vals.get('partner_invoice_id'):

                vals['partner_invoice_id'] = vals.get(
                    'partner_id',
                    record.partner_id and record.partner_id.id,
                )

        return super(AccountInvoice, self).write(vals)

    @api.model
    def _init_invoicing_address(self):
        invoices = self.search([('partner_invoice_id', '=', False)])

        for invoice in invoices:
            # This check should be obsolete due to the search filter
            if invoice.partner_invoice_id:
                continue

            invoice.partner_invoice_id = invoice.partner_id
