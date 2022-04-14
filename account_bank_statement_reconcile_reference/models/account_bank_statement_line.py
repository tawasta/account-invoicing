from odoo import models, api
from odoo.tools import float_round, float_repr


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    @api.model
    def create(self, vals):
        if vals.get("ref"):
            # If reference is given and an invoice can be found with it,
            # reference will be used as top priority
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
                vals["name"] = invoice.reference

        return super(AccountBankStatementLine, self).create(vals)

        return super(AccountBankStatementLine, self).create(vals)
