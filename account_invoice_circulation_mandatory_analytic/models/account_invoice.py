# -*- coding: utf-8 -*-
from odoo import models, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    def action_invoice_approve(self):
        if not all(line.account_analytic_id for line in self.invoice_line_ids):
            msg = \
                _('Please add analytic accounts to all lines before approving')
            raise UserError(msg)

        return super(AccountInvoice, self).action_invoice_approve()
