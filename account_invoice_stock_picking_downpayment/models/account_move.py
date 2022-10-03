from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _compute_amount(self):
        res = super()._compute_amount()
        for record in self:
            for picking in record.stock_picking_ids:
                if not picking.has_open_invoices():
                    # When all the invoices for a picking are paid, change the picking priority
                    priority = (
                        self.env["ir.config_parameter"]
                        .sudo()
                        .get_param("stock.picking.completed.payment.priority")
                    )
                    picking.sudo().write({"priority": priority})

        return res
