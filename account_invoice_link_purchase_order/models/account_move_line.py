from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    purchase_line_qty_received = fields.Float(related="purchase_line_id.qty_received")
    purchase_line_qty_invoiced = fields.Float(related="purchase_line_id.qty_to_invoice")

    @api.onchange("purchase_line_id")
    def _onchange_purchase_line_id(self):
        for record in self:
            if record.purchase_line_id:
                record.analytic_distribution = (
                    record.purchase_line_id.analytic_distribution
                )
            else:
                record.analytic_distribution = False
