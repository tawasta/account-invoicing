# -*- coding: utf-8 -*-


from odoo import api, fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    origin = fields.Char(
        readonly=False
    )

    @api.multi
    def action_invoice_open(self):
        res = super(AccountInvoice, self).action_invoice_open()
        if self.type not in ['out_refund', 'out_invoice', 'in_refund']:
            self.comment += "\n" + (self.origin or '') + "\n" + \
                (self.analytic_account_id.display_name or '')
        return res
