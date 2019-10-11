# -*- coding: utf-8 -*-
from odoo import models, api
from odoo.tools import float_round, float_repr


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    @api.model
    def create(self, vals):
        # If name (label) is empty, use reference (and partner name)
        if not vals.get('name') or vals['name'] == '/' and vals.get('ref'):
            if vals.get('partner_name'):
                # Use format:
                # {partner_name}: {reference}
                vals['name'] = '%s: %s' % (vals['partner_name'], vals['ref'])
            else:
                # Use format:
                # {reference}
                vals['name'] = vals['ref']

        return super(AccountBankStatementLine, self).create(vals)

    def get_reconciliation_proposition(self, excluded_ids=None):
        """ Get reconciliation proposition by invoice reference """

        # Skip the default matching. When we are using invoice reference
        # matching, a no match is a better option than a false match.
        # The default matching also matches a line with matching amount
        '''
        res = super(AccountBankStatementLine,
                    self).get_reconciliation_proposition(excluded_ids)
        '''
        res = self.env['account.move.line']

        # Try to match via payment reference
        if self.ref:
            account_invoice = self.env['account.invoice']
            amount = self.amount_currency or self.amount
            company_currency = self.journal_id.company_id.currency_id
            st_line_currency = self.currency_id or self.journal_id.currency_id
            currency = (
                st_line_currency and st_line_currency != company_currency) \
                       and st_line_currency.id or False

            precision = st_line_currency and st_line_currency.decimal_places \
                        or company_currency.decimal_places

            # Match invoice via payment reference. Skip amount matching here
            invoice = account_invoice.search([
                ('ref_number', '=', self.ref),
                ('state', '=', 'open'),
            ], limit=1)
            # Limit 1 should be safe here, as payment reference are unique

            # HERE we could try to mactch via "structured refernce", but it
            # can be very ambiguous and lead to false matches

            # If invoice is not found, try to match via partner and amount
            # This might result in a false positive, if a partner has multiple
            # open invoices with same amount
            if not invoice and self.partner_id or self.partner_name:
                partner_id = self.partner_id
                if not self.partner_id:
                    # Partner id is not set. Try to match via partner name.
                    # This usually won't work, as the payer name rarely exactly
                    # match to the invoice partner name
                    partner_ids = self.env['res.partner'].search([
                        ('name', '=ilike', self.partner_name),
                    ])

                    if len(partner_ids) == 1:
                        # If we are finding more than one matches, don't
                        # automatically match. That could be a false match
                        partner_id = partner_ids[0]

                if partner_id:
                    # Only try to match if partner id is set

                    # The paymennt amount won't necessarily have the same
                    # amount of decimals as the invoice
                    amount = float_repr(
                        float_round(amount, precision_digits=precision),
                        precision_digits=precision)

                    invoice = account_invoice.search([
                        ('amount_total', '=', amount),
                        ('partner_id', '=', partner_id.id),
                        ('state', '=', 'open'),
                    ], limit=1, order='date_due')
                    # Multiple matches can be found if partner and amount are
                    # the same, but if there is no payment reference, it
                    # shouldn't matter which invoice is paid. We choose the one
                    # with oldest due date

            if invoice and invoice.move_id:
                # An invoice is found, and it has an account move

                # Filter moves that are for receivable accounts
                moves = invoice.move_id.line_ids.filtered(
                    lambda r: r.account_id.user_type_id.type == 'receivable')

                if moves:
                    res = moves[0]

        return res
