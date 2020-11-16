
from odoo import fields, models


class AccountInvoiceReport(models.Model):

    _inherit = 'account.invoice.report'

    shipping_country_id = fields.Many2one(
        'res.country', string="Delivery Address' Country")

    def _from(self):
        # Adds Delivery address to from-clause
        return super(AccountInvoiceReport, self)._from() +\
            """JOIN res_partner shipping_ai ON
            ai.partner_shipping_id = shipping_ai.id"""

    def _group_by(self):
        return super(AccountInvoiceReport, self)._group_by() +\
            ", shipping_ai.country_id"

    def _select(self):
        return super(AccountInvoiceReport, self)._select() +\
            ", sub.shipping_country_id as shipping_country_id"

    def _sub_select(self):
        return super(AccountInvoiceReport, self)._sub_select() +\
            ", shipping_ai.country_id AS shipping_country_id"
