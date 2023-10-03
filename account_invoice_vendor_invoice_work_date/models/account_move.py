from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    work_date = fields.Date("Work Date", copy=False)
