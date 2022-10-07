from odoo import fields, models


class AccountInvoiceReport(models.Model):

    _inherit = "account.invoice.report"

    shipping_country_id = fields.Many2one(
        "res.country", string="Delivery Address Country"
    )

    def _from(self):
        # Adds Delivery address to from-clause
        return (
            super(AccountInvoiceReport, self)._from()
            + """LEFT JOIN res_partner shipping_am ON
            shipping_am.id = move.partner_shipping_id"""
        )

    def _select(self):
        return (
            super(AccountInvoiceReport, self)._select()
            + ", shipping_am.country_id AS shipping_country_id"
        )
