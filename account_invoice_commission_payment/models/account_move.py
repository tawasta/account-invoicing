from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    commission_payment_ids = fields.Many2many(
        comodel_name="account.payment",
        relation="account_move_account_payment_commission_rel",
        compute="_compute_commission_payment_ids",
        string="Commission Payments",
    )

    commission_payment_count = fields.Integer(
        compute="_compute_commission_payment_ids",
    )

    def _compute_commission_payment_ids(self):
        for move in self:
            commission_payment_ids = self.env["account.payment"].search(
                [("commission_move_line_ids.move_id", "in", move.ids)]
            )
            vals = {
                "commission_payment_ids": commission_payment_ids,
                "commission_payment_count": len(commission_payment_ids),
            }

            move.update(vals)

    def action_view_commission_payments(self):
        action = {
            "name": self.env._("Commission Payments"),
            "view_type": "form",
            "view_mode": "list,form",
            "res_model": "account.payment",
            "view_id": False,
            "type": "ir.actions.act_window",
            "domain": [("id", "in", self.commission_payment_ids.ids)],
        }

        return action
