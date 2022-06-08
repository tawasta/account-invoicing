from odoo import _, fields, models


class AccountPayment(models.Model):

    _inherit = "account.payment"

    commission_invoice_ids = fields.One2many(
        comodel_name="account.invoice",
        inverse_name="commission_payment_id",
        string="Commission invoices",
    )

    def button_commission_invoices(self):
        action = {
            "name": _("Commission Invoices"),
            "view_type": "form",
            "view_mode": "tree",
            "res_model": "account.invoice",
            "view_id": False,
            "type": "ir.actions.act_window",
            "domain": [("id", "in", [x.id for x in self.commission_invoice_ids])],
            "views": [
                (
                    self.env.ref(
                        "account_invoice_commission_payment.invoice_tree_commission"
                    ).id,
                    "tree",
                ),
            ],
        }

        return action
