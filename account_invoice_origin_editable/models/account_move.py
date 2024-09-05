from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    invoice_origin = fields.Char(readonly=False, tracking=True)
