# -*- coding: utf-8 -*-
from odoo import api, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.onchange('partner_invoice_id')
    def onchange_partner_invoice_id(self):
        # Override onchange to use partner_invoice_id instead of partner_id

        self.payment_term_id = \
            self.partner_invoice_id.property_payment_term_id and \
            self.partner_invoice_id.property_payment_term_id.id or \
            False
