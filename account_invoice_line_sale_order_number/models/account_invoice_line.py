from odoo import api, fields, models


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    origin = fields.Char(related="invoice_id.origin")
