from odoo import api
from odoo import models


class AccountReconciliation(models.AbstractModel):
    _inherit = "account.reconciliation.widget"

    @api.model
    def get_bank_statement_line_data(self, st_line_ids, excluded_ids=None):
        res = super().get_bank_statement_line_data(st_line_ids, excluded_ids)
        new_lines = []

        for line in res.get("lines", {}):
            new_line = dict(line)

            if not line.get("st_line"):
                # Statement line is missing (this shouldn't happen)
                new_lines.append(new_line)
                continue

            if line["st_line"].get("partner_id"):
                # Partner is already matched
                new_lines.append(new_line)
                continue

            ref = line["st_line"].get("ref")
            invoice = False

            if ref:
                # Try to find an invoice with ref
                domain = [
                    "|",
                    ("ref_number", "=", ref),
                    ("ref_number", "=", ref.lstrip("0")),
                ]
                invoice = self.env["account.invoice"].search(domain, limit=1)
                if invoice:
                    new_line["st_line"]["partner_id"] = invoice.partner_id.id
                    new_line["st_line"]["partner_name"] = invoice.partner_id.name

            if not invoice and line["st_line"]["partner_name"]:
                # No ref, or couln't find an invoice with ref
                # Try to find a partner
                partner_ids = self.env["res.partner"].search(
                    [("name", "=ilike", self.partner_name)]
                )

                if len(partner_ids) == 1:
                    # If we are finding more than one matches, don't
                    # automatically match. That could be a false match
                    new_line["st_line"]["partner_id"] = partner_ids[0].id
                    new_line["st_line"]["partner_id"] = partner_ids[0].name

            new_lines.append(new_line)

        res["lines"] = new_lines

        return res
