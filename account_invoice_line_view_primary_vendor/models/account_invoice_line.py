# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    # Related/computed helper fields here
    primary_vendor_id = fields.Many2one(
        comodel_name='res.partner',
        related='product_id.primary_vendor_id',
        store=True,
    )
