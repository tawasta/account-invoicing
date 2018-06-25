# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    origin_invoice_id = fields.Many2one(
        string='Origin invoice',
        comodel_name='account.invoice',
        copy=False,
        readonly=True,
    )
