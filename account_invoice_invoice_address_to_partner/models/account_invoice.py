# -*- coding: utf-8 -*-
from odoo import api, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.model
    def create(self, vals):
        # After creating invoice, change the partner_id to partner_invoice_id
        # This is done AFTER the creation to allow all partner_id-automation
        # to be run before the change
        res = super(AccountInvoice, self).create(vals)

        res.partner_id = res.partner_invoice_id.id

        return res
