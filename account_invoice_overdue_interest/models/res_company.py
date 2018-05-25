# -*- coding: utf-8 -*-
from odoo import fields, models


class ResCompany(models.Model):

    _inherit = 'res.company'

    default_overdue_interest = fields.Float(
        string='Default overdue interest %',
        digits=(4, 2),
    )
