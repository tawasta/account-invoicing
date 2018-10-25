# -*- coding: utf-8 -*-
from odoo import api, models, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.multi
    def invoice_validate(self):
        self._check_invoice_payment_term()

        return super(AccountInvoice, self).invoice_validate()

    def _check_invoice_payment_term(self):
        for record in self:
            if not record.payment_term_id:
                raise UserError(
                    _('Please set a payment term before validating')
                )
