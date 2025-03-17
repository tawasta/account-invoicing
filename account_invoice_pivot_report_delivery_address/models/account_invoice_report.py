from odoo import fields, models


class AccountInvoiceReport(models.Model):

    _inherit = "account.invoice.report"

    partner_shipping_id = fields.Many2one("res.partner", string="Delivery Address")

    def _sub_select(self):
        return (
            super(AccountInvoiceReport, self)._sub_select()
            + ", ai.partner_shipping_id as partner_shipping_id"
        )

    def _select(self):
        return (
            super(AccountInvoiceReport, self)._select()
            + ", move.partner_shipping_id as partner_shipping_id"
        )
