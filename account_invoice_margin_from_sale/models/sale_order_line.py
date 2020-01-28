from odoo import api, models


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    @api.multi
    def _prepare_invoice_line(self, qty):

        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)

        if self.purchase_price:
            res.update({"purchase_price": self.purchase_price})

        return res
