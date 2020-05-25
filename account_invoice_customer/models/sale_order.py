from odoo import api, fields, models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    @api.multi
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()

        invoice_vals["partner_customer_id"] = self.partner_id.id

        return invoice_vals
