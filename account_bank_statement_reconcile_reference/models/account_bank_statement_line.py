# -*- coding: utf-8 -*-
from odoo import models, api


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    def get_reconciliation_proposition(self, excluded_ids=None):
        res = super(AccountBankStatementLine,
                    self).get_reconciliation_proposition(excluded_ids)

        # Try to match via payment reference
        if self.ref:
            # Match invoice
            invoice = self.env['account.invoice'].search([
                ('ref_number', '=', self.ref)
            ], limit=1)

            if invoice and invoice.move_id:
                # An invoice is found, and it has an account move

                # Filter moves that are for receivable accounts
                moves = invoice.move_id.line_ids.filtered(
                    lambda r: r.account_id.user_type_id.type == 'receivable')

                if moves:
                    res = moves[0]

        return res
