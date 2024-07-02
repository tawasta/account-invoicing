from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    invoice_due_date = fields.Date(
        string="Due Date (as a date)",
        readonly=True,
        index=True,
        copy=False,
        related="invoice_date_due",
        states={"draft": [("readonly", False)]},
    )
