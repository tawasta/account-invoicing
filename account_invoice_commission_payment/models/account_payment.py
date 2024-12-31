from odoo import _, fields, models
from odoo.exceptions import ValidationError


class AccountPayment(models.Model):
    _inherit = "account.payment"

    commission_move_line_ids = fields.One2many(
        comodel_name="account.move.line",
        inverse_name="commission_payment_id",
        string="Commissioned lines",
    )

    commission_method = fields.Selection(
        [("cost", "Cost price")],
        string="Commission method",
        default=False,
    )

    negative_amount = fields.Monetary(currency_field="currency_id", readonly=True)

    def button_commission_invoices(self):
        action = {
            "name": _("Commission Invoices"),
            "view_type": "form",
            "view_mode": "tree,form",
            "res_model": "account.move",
            "view_id": False,
            "type": "ir.actions.act_window",
            "domain": [
                ("id", "in", self.commission_move_line_ids.mapped("move_id").ids)
            ],
        }

        return action

    def button_commission_invoice_lines(self):
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

    def action_compute_commission_amount(self):
        for record in self:
            # Decide the cost for the payment
            if record.commission_method == "cost":
                invoices = record.commission_move_line_ids.filtered(
                    lambda r: r.move_id.move_type == "out_invoice"
                )
                refunds = record.commission_move_line_ids.filtered(
                    lambda r: r.move_id.move_type == "out_refund"
                )

                amount = sum(invoices.mapped("purchase_price_total")) - sum(
                    refunds.mapped("purchase_price_total")
                )

                if amount < 0:
                    record.negative_amount = amount
                    amount = 0

                record.amount = amount
            else:
                raise ValidationError(_("Commission method is not set."))

    def action_draft(self):
        res = super().action_draft()

        for record in self:
            record.commission_move_line_ids.write({"commission_paid": True})
            record.commission_move_line_ids.mapped("move_id")._compute_commission_paid()

        return res

    def action_cancel(self):
        res = super().action_cancel()

        for record in self:
            record.commission_move_line_ids.write({"commission_paid": False})
            record.commission_move_line_ids.mapped("move_id")._compute_commission_paid()

        return res

    def unlink(self):
        for record in self:
            record.commission_move_line_ids.write({"commission_paid": False})
            record.commission_move_line_ids.mapped("move_id")._compute_commission_paid()

        return super().unlink()
