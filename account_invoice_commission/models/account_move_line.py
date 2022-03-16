from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    commission_paid = fields.Boolean(
        string="Commission paid",
        default=False,
        copy=False,
        readonly=True,
    )
