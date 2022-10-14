from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    stock_picking_ids = fields.Many2many(
        comodel_name="stock.picking",
        string="Stock pickings",
        required=False,
        copy=False,
        compute="_compute_stock_picking_ids",
    )

    def _compute_stock_picking_ids(self):
        for record in self:
            # Get all related pickings
            stock_pickings = record.invoice_line_ids.mapped(
                "sale_line_ids.order_id.picking_ids"
            )
            record.stock_picking_ids = stock_pickings

    # @api.multi
    def action_invoice_paid(self):
        res = super().action_invoice_paid()
        for record in self:
            if record.stock_picking_ids and record.state == "paid":
                for picking in record.stock_picking_ids:
                    if not picking.has_open_invoices():
                        # When all the invoices for a picking are paid,
                        # set picking priority as 1
                        # TODO: configurable priority
                        picking.sudo().write({"priority": "0"})
        return res
