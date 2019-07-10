# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    # Related/computed helper fields here
    commercial_partner_id = fields.Many2one(
        string='Partner',
        comodel_name='res.partner',
        related='invoice_id.commercial_partner_id',
        store=True,
    )

    partner_id = fields.Many2one(
        string='Partner',
        comodel_name='res.partner',
        related='invoice_id.partner_id',
        store=True,
    )

    product_categ_id = fields.Many2one(
        string='Category',
        comodel_name='product.category',
        related='product_id.categ_id',
        store=True,
    )

    date_invoice = fields.Date(
        string='Invoice date',
        related='invoice_id.date_invoice',
        store=True,
    )

    user_id = fields.Many2one(
        string='Responsible',
        related='invoice_id.user_id',
        store=True,
    )

    # The states are hard coded, but they could be fetched from account invoice
    # model if that is necessary
    state = fields.Selection([
        ('draft', 'Draft'),
        ('proforma', 'Pro-forma'),
        ('proforma2', 'Pro-forma'),
        ('open', 'Open'),
        ('paid', 'Paid'),
        ('cancel', 'Cancelled'),
    ],
        string='State',
        related='invoice_id.state',
        store=True,
    )

    # Invoice types are hard coded here, but it's very unlikely that they would
    # differ in any version or installation
    invoice_type = fields.Selection([
        ('out_invoice', 'Customer Invoice'),
        ('in_invoice', 'Vendor Bill'),
        ('out_refund', 'Customer Refund'),
        ('in_refund', 'Vendor Refund'),
    ],
        string='Type',
        related='invoice_id.type',
        store=True,
    )
