from odoo import fields, models
from odoo.exceptions import UserError


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    payment_settled = fields.Boolean(string="Payment settled?")
