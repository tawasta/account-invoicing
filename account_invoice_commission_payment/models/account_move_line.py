from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    purchase_price_total = fields.Float(
        string="Cost total",
        compute="_compute_purchase_price_total",
        digits="Product Price",
    )

    commission_payment_id = fields.Many2one(
        "account.payment", string="Commission payment", copy=False
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

    def _compute_purchase_price_total(self):
        for record in self:
            record.purchase_price_total = record.purchase_price * record.quantity

    def action_unlink_commission(self):
        self.write(
            {
                "commission_payment_id": False,
                "commission_paid": False,
            }
        )
        self.move_id._compute_commission_paid()
