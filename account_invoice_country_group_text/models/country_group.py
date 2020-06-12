from odoo import fields, models


class CountryGroup(models.Model):

    _inherit = "res.country.group"

    account_invoice_text = fields.Text(
        string="Account Invoice Text",
        help="Text to be added on account invoices going to customers in this "
        + "country group.",
    )
