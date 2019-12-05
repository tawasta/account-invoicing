# -*- coding: utf-8 -*-
from odoo import models, api


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.model
    def create(self, vals):
        """ Force using commercial partner if it's not set """
        res = super(AccountInvoice, self).create(vals)

        if not res.commercial_partner_id:
            res.commercial_partner_id = res.partner_id.commercial_partner_id

        return res

