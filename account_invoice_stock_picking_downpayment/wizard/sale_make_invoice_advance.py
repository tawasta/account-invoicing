from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    def _create_invoice(self, order, so_line, amount):
        if self.advance_payment_method in ("percentage", "fixed"):
            priority = self.env["ir.config_parameter"].get_param(
                "stock.picking.waiting.payment.priority"
            )
            order.sudo().picking_ids.write({"priority": priority})

        return super()._create_invoice(order, so_line, amount)
