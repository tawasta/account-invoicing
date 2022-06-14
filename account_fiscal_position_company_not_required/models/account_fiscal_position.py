from odoo import fields, models


class AccountFiscalPosition(models.Model):

    _inherit = "account.fiscal.position"

    company_id = fields.Many2one(required=False, readonly=False, default=False)
