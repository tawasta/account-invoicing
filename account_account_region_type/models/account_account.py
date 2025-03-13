from odoo import fields, models


class AccountAccount(models.Model):

    _inherit = "account.account"

    region_type = fields.Selection(
        [
            ("domestic", "Domestic"),
            ("usa", "USA"),
            ("eu", "EU"),
            ("non_eu", "non-EU"),
        ],
        string="Region type",
        copy=False,
        default=False,
    )
