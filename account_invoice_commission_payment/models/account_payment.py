from odoo import fields
from odoo import models


class AccountPayment(models.Model):

    _inherit = "account.payment"

    commission_invoice_ids = fields.One2many(
        comodel_name="account.invoice",
        inverse_name="commission_payment_id",
        string="Commission invoices",
    )
