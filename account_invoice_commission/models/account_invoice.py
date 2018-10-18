# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    commission_paid = fields.Boolean(
        string='Commission paid',
        default=False,)
