
from odoo import api, fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    sale_order_ids = fields.Many2many(
        comodel_name='sale.order',
        relation='account_invoice_sale_order_rel',
        string='Related Sale Orders',
        compute='_compute_related_sale_order',
        readonly=True,
        copy=False
    )

    @api.depends('invoice_line_ids')
    def _compute_related_sale_order(self):
        for invoice in self:
            sale_order_ids = invoice.invoice_line_ids.\
                mapped('sale_line_ids').mapped('order_id')

            invoice.update({
                'sale_order_ids': sale_order_ids.ids
            })
