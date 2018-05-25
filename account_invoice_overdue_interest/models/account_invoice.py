# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id.overdue_interest:
            self.overdue_interest = self.partner_id.overdue_interest
        else:
            self.overdue_interest = self.company_id.default_overdue_interest

    overdue_interest = fields.Float(
        string='Overdue interest (%)',
        digits=(4, 2),
    )
