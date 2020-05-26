
from odoo import api, fields, models, _
from odoo.exceptions import UserError


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

    merge_order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Merge to order',
        help='Manually select an order to merge to',
        domain=[('state', 'in', ['draft', 'sent', 'sale'])],
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

    analytic_account = fields.Boolean(
        string='Analytic account from the first line?',
        default=True,
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

        # Placeholder for analytic account
        account_analytic_id = False

        # If order lines (type) is none, don't do any SO lines
        if self.order_lines != 'none':
            invoice = AccountInvoice.browse([invoice_id])

            if self.order_lines == 'copy':
                # Copy all lines from invoice to order
                for line in invoice.invoice_line_ids:
                    if self.analytic_account and not account_analytic_id:
                        # Use first line analytic id as order analytic id
                        account_analytic_id = line.account_analytic_id.id

                    # Check is invoice line's tax Included In Price

                    if len(line.invoice_line_tax_ids) > 1:
                        raise UserError(_('Too many taxes per line! The '
                                          'number of taxes per line should be '
                                          'one or none.'))

                    if line.invoice_line_tax_ids.price_include:
                        price = line.price_subtotal
                    else:
                        price = line.price_unit

                    order_lines.append((0, 0, dict(
                        product_id=line.product_id.id,
                        price_unit=price,
                        name=line.name,
                        product_uom_qty=line.quantity,
                        product_uom=line.uom_id.id,
                        analytic_tag_ids=line.analytic_tag_ids,
                    )))

            elif self.order_lines == 'merge':
                # Merge invoice lines to one sale order line
                price_unit = 0
                analytic_tag_ids = list()
                add_analytic_tags = True

                for line in invoice.invoice_line_ids:
                    if self.analytic_account and not account_analytic_id:
                        # Use first line analytic id as order analytic id
                        account_analytic_id = line.account_analytic_id.id

                    # Untaxed Amount will be the invoice subtotal
                    price_unit = invoice.amount_untaxed

                    for analytic in line.analytic_tag_ids:
                        if add_analytic_tags:
                            analytic_tag_ids.append(analytic.id)

                    if self.analytic_account:
                        # Only add the first row analytic tags
                        add_analytic_tags = False

                merged_line = dict(
                    product_id=self.product_id.id,
                    price_unit=price_unit,
                    product_uom_qty=1,
                    product_uom=self.product_id.uom_id.id,
                    analytic_tag_ids=[(6, 0, analytic_tag_ids)],
                )

                order_lines.append((0, 0, merged_line))

        if self.merge_order_id:
            # Manually selected order to merge
            sale_order = self.merge_order_id
        else:
            # Automatically selected order to merge
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
                related_project_id=account_analytic_id,
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
