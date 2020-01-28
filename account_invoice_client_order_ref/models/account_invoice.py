from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    client_order_ref = fields.Char("Customer Reference")
