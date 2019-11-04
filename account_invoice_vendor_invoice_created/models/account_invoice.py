from odoo import fields, models
from odoo.exceptions import UserError


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    vendor_invoice_created = fields.Boolean(string="Vendor invoice created?")
