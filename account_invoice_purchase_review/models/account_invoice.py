from odoo import models, fields, api


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    purchase_order_ids = fields.One2many(
        comodel_name='purchase.order',
        compute='_compute_purchase_order_ids',
        string='Related purchases',
    )

    @api.onchange('purchase_id')
    def purchase_order_change(self):
        """
        Override to disable auto-adding invoice lines
        """
        if not self.purchase_id:
            return {}
        if not self.partner_id:
            self.partner_id = self.purchase_id.partner_id.id

        vendor_ref = self.purchase_id.partner_ref
        if vendor_ref and (not self.reference or (
                vendor_ref + ", " not in self.reference and not self.reference.endswith(
                vendor_ref))):
            self.reference = ", ".join(
                [self.reference, vendor_ref]) if self.reference else vendor_ref

        if not self.invoice_line_ids:
            self.payment_term_id = self.purchase_id.payment_term_id
            # as there's no invoice line yet, we keep the currency of the PO
            self.currency_id = self.purchase_id.currency_id

        for line in self.purchase_id.order_line - self.invoice_line_ids.mapped(
                'purchase_line_id'):

            # Difference to core version starts here
            line_match = self.invoice_line_ids.filtered(
                lambda r:
                r.quantity == line.product_qty
                and r.price_unit == line.price_unit
            )

            if len(line_match) == 1:
                line_match.purchase_id = line.order_id.id
                line_match.purchase_line_id = line.id

        self.env.context = dict(self.env.context,
                                from_purchase_order_change=True)
        self.purchase_id = False

        return {}

    def _compute_purchase_order_ids(self):
        for record in self:
            record.purchase_order_ids = \
                record.invoice_line_ids.mapped('purchase_id').ids
