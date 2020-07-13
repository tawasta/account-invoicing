from odoo import fields, models


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    sale_order_ids = fields.One2many(related="invoice_id.sale_order_ids")

    sale_order_numbers = fields.Char(compute="_compute_sale_order_numbers",)

    def _compute_sale_order_numbers(self):
        for record in self:
            numbers = ""
            for sale_order in self.sale_order_ids:
                numbers = "{} {}".format(numbers, sale_order.name,)

            record.sale_order_numbers = numbers
