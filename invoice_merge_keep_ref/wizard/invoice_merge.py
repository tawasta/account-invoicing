from odoo import fields, models


class InvoiceMergeCustom(models.TransientModel):
    _inherit = "invoice.merge"

    keep_original_refs = fields.Boolean(string="Keep customer references")

    def merge_invoices(self):
        old_ids = self.env.context.get("active_ids", [])
        invoices = self.env["account.move"].browse(old_ids)

        # Talleta alkuperäisten ref-arvot
        refs = list(filter(None, invoices.mapped("ref")))  # Poistaa tyhjät

        # Suorita alkuperäinen yhdistys
        res = super().merge_invoices()

        # Selvitä uusi lasku
        invoice_domain = res.get("domain")
        all_ids = invoice_domain[0][2]
        new_invoice_ids = [inv_id for inv_id in all_ids if inv_id not in old_ids]

        if self.keep_original_refs and new_invoice_ids:
            new_invoices = self.env["account.move"].browse(new_invoice_ids)
            for invoice in new_invoices:
                # Säilytetään olemassa oleva ref (jos sellainen on) ja yhdistetään
                existing_ref = invoice.ref or ""
                combined_refs = ", ".join(refs)
                if existing_ref:
                    invoice.ref = f"{existing_ref}, {combined_refs}"
                else:
                    invoice.ref = combined_refs

        return res
