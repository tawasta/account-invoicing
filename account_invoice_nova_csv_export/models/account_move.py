from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    last_nova_csv_export = fields.Datetime(
        string="Last Nova CSV Export Date",
        help="When this invoice was last exported into a CSV file.",
    )
