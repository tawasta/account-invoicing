from odoo import api, models


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        if self.advance_payment_method in ("percentage", "fixed"):
            # TODO: configurable priority
            order.sudo().picking_ids.write({"priority": "4"})

        return super()._create_invoice(
            order, so_line, amount
        )
