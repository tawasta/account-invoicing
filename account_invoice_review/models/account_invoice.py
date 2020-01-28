from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    reviewed = fields.Boolean("Reviewed")
