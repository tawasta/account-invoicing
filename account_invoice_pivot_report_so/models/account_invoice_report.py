from odoo import fields, models


class AccountInvoiceReport(models.Model):

    _inherit = "account.invoice.report"

    sale_id = fields.Many2one("sale.order", readonly=True, string="SO-number")

    def _from(self):
        return (
            super(AccountInvoiceReport, self)._from()
            + """
           LEFT JOIN sale_order order_sale ON
                order_sale.id =
                (SELECT DISTINCT so.id
                    FROM sale_order so
                    JOIN sale_order_line sol ON sol.order_id = so.id
                    JOIN sale_order_line_invoice_rel soli_rel ON soli_rel.order_line_id = sol.id
                    JOIN account_move_line aml ON aml.id = soli_rel.invoice_line_id
                    JOIN account_move am ON am.id = aml.move_id
                WHERE
                    am.move_type in ('out_invoice', 'out_refund') AND
                    am.id = move.id)
            """
        )

    def _select(self):
        return (
            super(AccountInvoiceReport, self)._select() + ", order_sale.id as sale_id"
        )
