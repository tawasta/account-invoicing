from odoo import fields, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    tax_report = fields.Boolean(help="Available for tax report")
