# -*- coding: utf-8 -*-
from odoo import fields, models


class ResCompany(models.Model):

    _inherit = 'res.company'

    default_notice_period = fields.Integer(
        string='Notice period (days)',
        help='Default notice period (days) for new customers and invoices',
    )
