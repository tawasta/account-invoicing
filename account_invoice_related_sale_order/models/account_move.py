from odoo import api, fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    sale_order_ids = fields.Many2many(
        comodel_name="sale.order",
        relation="account_invoice_sale_order_rel",
        string="Related Sale Orders",
        compute="_compute_related_sale_order",
        readonly=True,
        copy=False,
    )

    sale_id = fields.Many2one(
        "sale.order",
        related="invoice_line_ids.sale_line_ids.order_id",
    )

    @api.depends("invoice_line_ids")
    def _compute_related_sale_order(self):
        for move in self:
            sale_order_ids = move.invoice_line_ids.mapped("sale_line_ids").mapped(
                "order_id"
            )
            move.update({"sale_order_ids": sale_order_ids.ids})
