# -*- coding: utf-8 -*-
from odoo import api, models
from collections import OrderedDict


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.model
    def _get_first_invoice_fields(self, invoice):

        res = super(AccountInvoice, self)._get_first_invoice_fields(
            invoice=invoice
        )

        res['invoice_line_ids'] = OrderedDict()

        return res
