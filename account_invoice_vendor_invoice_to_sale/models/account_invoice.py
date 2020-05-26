from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

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
