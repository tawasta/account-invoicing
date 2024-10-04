from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    linked_sale_line_ids = fields.One2many(
        string="Related sale lines",
        comodel_name="sale.order.line",
        inverse_name="linked_account_move_id",
        copy=False,
    )

    sale_order_ids = fields.One2many(
        string="Related sales",
        comodel_name="sale.order",
        inverse_name="origin_invoice_id",
        copy=False,
    )

    def action_create_sale_order(self):
        self.ensure_one()

        return {
            "type": "ir.actions.act_window",
            "res_model": "invoice.to.sale",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_origin": self.number,
                "default_origin_invoice_id": self.id,
            },
        }
