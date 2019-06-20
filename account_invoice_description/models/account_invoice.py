# -*- coding: utf-8 -*-


from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    description = fields.Text(string="Invoice description")
