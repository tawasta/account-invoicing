from odoo import fields, models


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    origin = fields.Char(related="invoice_id.origin", store=True)
