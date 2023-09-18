from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    work_description = fields.Text("Work Description", copy=False)
