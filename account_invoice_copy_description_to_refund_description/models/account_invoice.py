# -*- coding: utf-8 -*-


from odoo import api, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.model
    def _prepare_refund(self, invoice, date_invoice=None, date=None,
                        description=None, journal_id=None):

        res = super(AccountInvoice, self)._prepare_refund(
            invoice, date_invoice=date_invoice, date=date,
            description=description, journal_id=journal_id,
        )

        if res.get('name'):
            res['name'] = self.name or ''

        return res
