from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    picking_ids = fields.Many2many(
        comodel_name='stock.picking',
        string='Pickings',
        compute='_compute_picking_ids',
    )

    def _compute_picking_ids(self):
        for record in self:
            record.picking_ids = record.invoice_line_ids.mapped(
                'sale_line_ids.order_id.picking_ids')
