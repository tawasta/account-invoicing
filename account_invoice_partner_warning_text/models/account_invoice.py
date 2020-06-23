
from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    invoice_warn_msg = fields.Text(related="partner_customer_id.invoice_warn_msg")
