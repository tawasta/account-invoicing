from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    warranty = fields.Boolean(string="Warranty case", default=False)
