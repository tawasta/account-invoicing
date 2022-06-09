from babel.dates import format_date

from odoo import api, models


class InvoiceMerge(models.TransientModel):

    _inherit = "invoice.merge"

    def _get_line_info(self, line):
        info = ", ".join(
            [
                "{}, {}".format(
                    self._get_order_date_with_locale(sol), sol.order_id.name
                )
                for sol in line.sale_line_ids
            ]
        )

        info_str = " (%s)" % info if info else ""

        return info_str

    def _get_order_date_with_locale(self, sale_line):
        order_date = sale_line.order_id.date_order

        order_date_with_locale = format_date(
            order_date, format="short", locale=sale_line.order_id.partner_id.lang
        )

        return order_date_with_locale

    @api.multi
    def merge_invoices(self):
        # Modify the invoice line descriptions before doing the merge,
        # account_invoice_merge module handles the rest.
        ids = self.env.context.get("active_ids", [])
        invoices = self.env["account.invoice"].browse(ids)

        for invoice in invoices:
            for line in invoice.invoice_line_ids:
                line.name = line.name + self._get_line_info(line)

        return super(InvoiceMerge, self).merge_invoices()
