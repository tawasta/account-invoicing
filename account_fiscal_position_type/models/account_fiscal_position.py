from odoo import fields, models


class AccountFiscalPosition(models.Model):

    _inherit = "account.fiscal.position"

    fiscal_type = fields.Selection(
        [
            ("domestic", "Domestic"),
            ("eu", "EU"),
            ("non_eu", "non-EU"),
        ],
        string="Type",
        copy=False,
        default=False,
    )
