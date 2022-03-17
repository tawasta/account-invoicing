from odoo import _
from odoo import fields
from odoo import models


class AccountPayment(models.Model):

    _inherit = "account.payment"

    commission_move_line_ids = fields.One2many(
        comodel_name="account.move.line",
        inverse_name="commission_payment_id",
        string="Commission invoices",
    )

    def button_commission_invoices(self):
        action = {
            "name": _("Commission Invoice lines"),
            "view_type": "form",
            "view_mode": "tree",
            "res_model": "account.move.line",
            "view_id": False,
            "type": "ir.actions.act_window",
            "domain": [("id", "in", [x.id for x in self.commission_move_line_ids])],
            "views": [
                (
                    self.env.ref(
                        "account_invoice_commission_payment.move_line_tree_commission"
                    ).id,
                    "tree",
                ),
            ],
        }

        return action

    def action_cancel(self):
        res = super().action_cancel()

        for record in self:
            for line in record.commission_move_line_ids:
                line.commission_paid = False
                line.onchange_commission_paid()

        return res

    def action_draft(self):
        res = super().action_draft()

        for record in self:
            for line in record.commission_move_line_ids:
                line.commission_paid = True
                line.onchange_commission_paid()

        return res
