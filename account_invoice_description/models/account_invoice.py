from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    description = fields.Text(
        string="Internal note",
        help="Not shown to partner.",
    )
