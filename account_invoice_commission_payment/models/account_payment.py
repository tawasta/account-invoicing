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
