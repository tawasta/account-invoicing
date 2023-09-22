from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    work_title = fields.Char("Work Title", copy=False)
