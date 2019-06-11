# -*- coding: utf-8 -*-
from odoo import models, api


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    @api.multi
    def write(self, vals):
        res = super(AccountInvoiceLine, self).write(vals)

        res._member_line_partner_from_anaytic_account()

        return res

    @api.model
    def create(self, vals):
        res = super(AccountInvoiceLine, self).create(vals)

        res._member_line_partner_from_anaytic_account()

        return res

    def _member_line_partner_from_anaytic_account(self):
        """Change the member line partner, if analytic account is set."""
        member_line = self.env['membership.membership_line']

        for record in self:
            analytic = record.account_analytic_id
            member_lines = member_line.search([
                ('account_invoice_line', '=', record.id)
            ])

            if member_lines and analytic and analytic.partner_id:
                for member_line in member_lines:
                    # Generally there shouldn't be more than one line
                    member_line.partner = analytic.partner_id.id
