# -*- coding: utf-8 -*-
from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    margin = fields.Monetary(
        compute='_compute_product_margin',
        help='It gives profitability by calculating the difference between '
             'the Unit Price and the cost.',
        currency_field='currency_id',
        digits=dp.get_precision('Product Price'),
        store=True)

    @api.depends('invoice_line_ids.margin')
    def _compute_product_margin(self):
        for invoice in self:
            margin = sum(invoice.invoice_line_ids.filtered(
                lambda r: r.invoice_id.state != 'cancel').mapped('margin'))
            sign = invoice.type in ['in_refund', 'out_refund'] and -1 or 1
            invoice.margin = sign * margin
