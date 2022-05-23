from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    vendor_invoice_created = fields.Boolean(string="Vendor invoice created?")
