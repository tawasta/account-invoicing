# -*- coding: utf-8 -*-
from odoo import models, api, fields


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    percent = fields.Float(
        string='Percent',
        compute='_compute_percent')

    @api.depends('margin', 'amount_untaxed')
    def _compute_percent(self):
        for invoice in self:
            if invoice.margin and invoice.amount_untaxed:
                sign = invoice.type in ['in_refund', 'out_refund'] and -1 or 1
                invoice.percent \
                    = sign * (invoice.margin / invoice.amount_untaxed) * 100
