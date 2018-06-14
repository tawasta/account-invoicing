# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    origin_invoice_ids = fields.One2many(
        string='Origin invoices',
        comodel_name='account.invoice',
        inverse_name='sale_order_id',
    )
