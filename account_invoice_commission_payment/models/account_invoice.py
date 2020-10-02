from odoo import fields
from odoo import models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    commission_payment_id = fields.Many2one(
        "account.payment", string="Commission payment"
    )
