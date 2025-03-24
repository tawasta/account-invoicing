from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoices(self, sale_orders):
        if self.advance_payment_method in ("percentage", "fixed"):
            priority = (
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("stock.picking.waiting.payment.priority")
            )
            for order in sale_orders:
                order.sudo().picking_ids.write({"priority": priority})

        return super()._create_invoices(sale_orders)
