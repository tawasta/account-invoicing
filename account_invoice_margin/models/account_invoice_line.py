# -*- coding: utf-8 -*-
from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class AccountInvoiceLine(models.Model):

    _inherit = "account.invoice.line"

    margin = fields.Float(
        compute='_compute_product_margin',
        digits=dp.get_precision('Product Price'),
        store=True
    )

    purchase_price = fields.Float(
        string='Cost',
        digits=dp.get_precision('Product Price')
    )

    def _compute_margin(self, invoice_id, product_id, product_uom_id):
        frm_cur = self.env.user.company_id.currency_id
        to_cur = invoice_id.currency_id
        purchase_price = product_id.standard_price
        if product_uom_id != product_id.uom_id:
            purchase_price = product_id.uom_id._compute_price(purchase_price,
                                                              product_uom_id)
        ctx = self.env.context.copy()
        ctx['date'] = invoice_id.date_invoice
        price = frm_cur.with_context(ctx).compute(purchase_price,
                                                  to_cur,
                                                  round=False)
        return price

    @api.onchange('product_id', 'uom_id')
    def product_id_change_margin(self):
        if not self.product_id or not self.uom_id:
            return
        self.purchase_price \
            = self._compute_margin(self.invoice_id,
                                   self.product_id,
                                   self.uom_id)

    @api.model
    def create(self, vals):
        # Calculation of the margin for programmatic creation of a line.
        # It is therefore not necessary to call product_id_change_margin
        # manually
        if 'purchase_price' not in vals:
            invoice_id \
                = self.env['account.invoice'].browse(vals['invoice_id'])
            product_id \
                = self.env['product.product'].browse(vals['product_id'])
            product_uom_id = self.env['product.uom'].browse(vals['uom_id'])

            vals['purchase_price'] = self._compute_margin(invoice_id,
                                                          product_id,
                                                          product_uom_id)

        return super(AccountInvoiceLine, self).create(vals)

    @api.depends('product_id', 'purchase_price', 'quantity',
                 'price_unit', 'price_subtotal')
    def _compute_product_margin(self):
        for line in self:

            if line.invoice_id.type not in ['out_invoice', 'out_refund']:
                line.margin = 0.00
            else:
                currency = line.invoice_id.currency_id
                price = line.purchase_price
                if not price:
                    from_cur \
                        = line.env.user.company_id.currency_id.with_context(
                            date=line.invoice_id.date_invoice)
                    price = from_cur.compute(
                        line.product_id.standard_price, currency, round=False)

                line.margin = currency.round(
                    line.price_subtotal - (price * line.quantity))
