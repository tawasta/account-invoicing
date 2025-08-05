from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def do_merge(
        self, keep_references=True, date_invoice=False, remove_empty_invoice_lines=True
    ):
        """Adds Customer reference information to a merged invoice"""
        invoices_info = super().do_merge(
            keep_references, date_invoice, remove_empty_invoice_lines
        )

        old_invoice_ids = next(iter(invoices_info.values()))
        new_invoice_id = next(iter(invoices_info))
        new_invoice = self.env["account.move"].browse(new_invoice_id)

        refs = []

        for invoice_id in old_invoice_ids:
            invoice = self.env["account.move"].browse(invoice_id)

            if invoice.ref and invoice.ref not in refs:
                refs.append(invoice.ref)
        if refs:
            new_invoice.ref = ", ".join(refs)

        return invoices_info
