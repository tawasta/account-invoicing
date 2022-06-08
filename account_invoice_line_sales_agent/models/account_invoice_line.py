from odoo import fields, models


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    sales_agent = fields.Many2one(
        related="invoice_id.sales_agent",
        store=True,
    )
