from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    commission_paid = fields.Boolean(string="Commission paid", default=False)
