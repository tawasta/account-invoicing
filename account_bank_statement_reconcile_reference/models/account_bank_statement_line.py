from odoo import models, api
from odoo.tools import float_round, float_repr


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    @api.model
    def create(self, vals):
        # If name (label) is empty, use reference (and partner name)
        if not vals.get("name") or vals["name"] in ["/", "-"] and vals.get("ref"):
            if vals.get("partner_name"):
                # Use format:
                # {partner_name}: {reference}
                vals["name"] = "%s: %s" % (vals["partner_name"], vals["ref"])
            else:
                # Use format:
                # {reference}
                vals["name"] = vals["ref"]

        if not vals.get("partner_id") and vals.get("ref"):
            invoice = self.env["account.invoice"].search(
                [
                    "|",
                    ("ref_number", "=", vals["ref"]),
                    ("ref_number", "=", vals["ref"].lstrip("0")),
                ],
                limit=1,
            )
            if invoice:
                vals["partner_id"] = invoice.partner_id.id

        return super(AccountBankStatementLine, self).create(vals)
