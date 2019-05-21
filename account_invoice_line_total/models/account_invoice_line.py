# -*- coding: utf-8 -*-
from odoo import fields, models, api


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    price_total = fields.Monetary(
        string='Taxable amount',
        readonly=True,
        compute='_compute_price_total'
    )

    @api.multi
    def _compute_price_total(self):
        for record in self:
            currency = record.invoice_id and record.invoice_id.currency_id \
                or None
            price = record.price_unit * (1 - (record.discount or 0.0) / 100.0)
            taxes = False

            if record.invoice_line_tax_ids:
                taxes = record.invoice_line_tax_ids.compute_all(
                    price,
                    currency,
                    record.quantity,
                    product=record.product_id,
                    partner=record.invoice_id.partner_id
                )

            record.price_total = taxes['total_included'] if \
                taxes else \
                record.quantity * price
