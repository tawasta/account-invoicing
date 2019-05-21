# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    client_order_ref = fields.Char('Customer Reference')
