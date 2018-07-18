# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    def _get_default_notice_period(self):
        if self.company_id:
            return self.company_id.default_notice_period
        else:
            return self.env.user.company_id.default_notice_period

    notice_period = fields.Integer(
        string='Notice period (days)',
        default=_get_default_notice_period,
        help='Default notice period (days) for new customers and invoices',
    )
