from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    vendor_invoice_created = fields.Boolean(string="Vendor invoice created?")
