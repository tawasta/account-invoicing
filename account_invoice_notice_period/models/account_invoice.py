# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    notice_period = fields.Integer(
        string='Notice period (days)',
        help='Default notice period (days) for new customers and invoices',
    )

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.notice_period = self.partner_id.notice_period \
            or self.company_id.default_notice_period
