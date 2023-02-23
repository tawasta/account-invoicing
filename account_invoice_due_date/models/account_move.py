from odoo import fields, models, api


class AccountMove(models.Model):

    _inherit = "account.move"

    invoice_due_date = fields.Date(string='Due Date', readonly=True, index=True, copy=False, related='invoice_date_due',
        states={'draft': [('readonly', False)]})


