from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    description = fields.Text(
        string="Internal note",
        help="Not shown to partner.",
    )
