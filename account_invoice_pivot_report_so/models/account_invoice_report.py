from odoo import api, fields, models
from odoo.tools import SQL


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    sale_id = fields.Many2one("sale.order", readonly=True, string="Sale Order Number")

    @api.model
    def _from(self) -> SQL:
        # The sale order is taken per invoice line: one invoice can contain lines
        # of several sale orders. MIN keeps one order if a line has several.
        return SQL(
            """%s
            LEFT JOIN LATERAL (
                SELECT MIN(sol.order_id) AS id
                FROM sale_order_line_invoice_rel soli_rel
                JOIN sale_order_line sol ON sol.id = soli_rel.order_line_id
                WHERE soli_rel.invoice_line_id = line.id
            ) order_sale ON TRUE
            """,
            super()._from(),
        )

    @api.model
    def _select(self) -> SQL:
        return SQL("%s, order_sale.id AS sale_id", super()._select())
