from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    partner_customer_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer",
        readonly=True,
        states={"draft": [("readonly", False)]},
        track_visibility="always",
    )
