# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountInvoiceCirculation(models.Model):

    _name = 'account.invoice.circulation'

    name = fields.Char(
        string='Invoice circulation',
        required=True,
    )

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Validator',
        required=True,
    )

    circulation_line_ids = fields.One2many(
        comodel_name='account.invoice.circulation.line',
        inverse_name='circulation_id',
        string='Approvers',
    )
