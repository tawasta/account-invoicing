# -*- coding: utf-8 -*-
from odoo import models, fields, api


class InvoiceToSale(models.TransientModel):
    _name = "invoice.to.sale"

    auto_confirm = fields.Boolean(
        default=True,
        string='Auto-confirm sale order?',
        help='Uncheck this if you want to leave the sale order as draft'
    )

    merge_order = fields.Boolean(
        string='Merge order to existing?',
        help='Uncheck this if you want to always create a new sale order',
        default=True,
    )

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        required=True,
    )

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsible',
        required=True,
    )

    order_lines = fields.Selection(
        string='Order lines',
        selection=[
            ('none', 'No lines (empty sale order)'),
            ('copy', 'Copy lines (use the products on the invoice)'),
            ('merge', 'Merge lines (select a new product)'),
        ],
        default='none',
        required=True,
    )

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
    )

    @api.multi
    def confirm(self):
        # Create SO from invoice

        SaleOrder = self.env['sale.order']
        AccountInvoice = self.env['account.invoice']

        # Source invoice
        invoice_id = self._context.get('active_id')

        # Decide product lines
        order_lines = []

        # If order lines (type) is none, don't do any SO lines
        if self.order_lines != 'none':
            invoice = AccountInvoice.browse([invoice_id])

            if self.order_lines == 'copy':
                # Copy all lines from invoice to order
                for line in invoice.invoice_line_ids:
                    order_lines.append((0, 0, dict(
                        product_id=line.product_id.id,
                        price_unit=line.price_unit,
                        name=line.name,
                        product_uom_qty=line.quantity,
                        product_uom=line.uom_id.id,
                        analytic_account_id=line.analytic_account_id.id,
                        analytic_tag_ids=line.analytic_tag_ids,
                    )))

            elif self.order_lines == 'merge':
                # Merge invoice lines to one sale order line
                price_unit = 0
                analytic_tag_ids = list()

                for line in invoice.invoice_line_ids:
                    price_unit += line.price_unit * line.quantity

                    for analytic in line.analytic_tag_ids:
                        analytic_tag_ids.append(analytic.id)

                merged_line = dict(
                    product_id=self.product_id.id,
                    price_unit=price_unit,
                    product_uom_qty=1,
                    product_uom=self.product_id.uom_id.id,
                    analytic_tag_ids=[(6, 0, analytic_tag_ids)],
                )

                order_lines.append((0, 0, merged_line))

        # Check if a sale order exists
        sale_order = SaleOrder.search([
            ('origin_invoice_id', '=', invoice_id),
            ('state', 'in', ['draft', 'sent', 'sale']),
        ], limit=1)

        if self.merge_order and sale_order:
            # Merge lines to an existing order
            sale_order.order_line = order_lines
        else:
            # Create a new order
            values = dict(
                origin_invoice_id=invoice_id,
                partner_id=self.partner_id.id,
                user_id=self.user_id.id,
                order_line=order_lines,
            )

            sale_order = SaleOrder.create(
                values,
            )

        # Auto-confirm order
        if self.auto_confirm and sale_order.state in ['draft', 'sent']:
            sale_order.action_confirm()

        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'target': 'current',
            'res_id': sale_order.id,
            'type': 'ir.actions.act_window',
        }
