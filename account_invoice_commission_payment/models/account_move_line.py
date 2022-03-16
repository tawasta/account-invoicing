from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    commission_payment_id = fields.Many2one(
        "account.payment", string="Commission payment"
    )

    commission_payment_state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("posted", "Posted"),
            ("cancel", "Cancelled"),
        ],
        string="Commission",
        help="Commission payment state",
        related="commission_payment_id.state",
        readonly=True,
        copy=False,
        default="draft",
    )
