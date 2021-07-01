from odoo import api, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.multi
    def do_merge(
        self, keep_references=True, date_invoice=False, remove_empty_invoice_lines=True
    ):

        res = super().do_merge(
            keep_references, date_invoice, remove_empty_invoice_lines
        )

        new_invoice_id = list(res.keys())
        new_invoice = self.browse(new_invoice_id)

        for line in new_invoice.invoice_line_ids:
            line.purchase_price = line.product_id.standard_price

        return res
