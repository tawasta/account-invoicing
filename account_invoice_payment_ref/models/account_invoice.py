from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    invoice_payment_ref = fields.Char(
        string='Payment Reference',
        index=True,
        copy=False,
        help="The payment reference to set on journal items."
    )
