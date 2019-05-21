# -*- coding: utf-8 -*-
from odoo import models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    def _get_invoice_line_key_cols(self):
        res = super(AccountInvoice, self)._get_invoice_line_key_cols()

        res.append('id')

        return res
