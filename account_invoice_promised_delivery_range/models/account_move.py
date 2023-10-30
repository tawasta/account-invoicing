from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    date_delivery_promised_start = fields.Date(
        string="Promised Delivery start",
        readonly=True,
        states={"draft": [("readonly", False)]},
        copy=False,
    )

    date_delivery_promised_end = fields.Date(
        string="Promised Delivery end",
        readonly=True,
        states={"draft": [("readonly", False)]},
        copy=False,
    )
