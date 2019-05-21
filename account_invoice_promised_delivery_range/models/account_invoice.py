# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):

    _inherit = 'account.invoice'

    date_delivery_promised_start = fields.Date(
        string='Promised Delivery start',
        readonly=True,
        states={
            'draft': [('readonly', False)],
            'sent': [('readonly', False)]
        },
        copy=False,
    )

    date_delivery_promised_end = fields.Date(
        string='Promised Delivery end',
        readonly=True,
        states={
            'draft': [('readonly', False)],
            'sent': [('readonly', False)]
        },
        copy=False,
    )
