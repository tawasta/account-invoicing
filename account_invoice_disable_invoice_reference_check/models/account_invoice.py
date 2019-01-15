# -*- coding: utf-8 -*-
from odoo import models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    # Override invoice reference check
    def _check_invoice_reference(self):
        return True
