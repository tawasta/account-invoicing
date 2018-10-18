# -*- coding: utf-8 -*-
from odoo import models, api, _


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    @api.onchange('quantity', 'price_unit')
    def onchange_check_negative_values(self):

        res = dict()
        if self.invoice_id.type in ['in_refund', 'out_refund']:
            if self.quantity < 0 or self.price_unit < 0:
                msg = _("Please use positive values for refund "
                        "lines' prices and quantities. The conversion "
                        "to negative values is done automatically.")
                warning = dict(
                    title=_('Warning'),
                    message=msg
                )
                res['warning'] = warning

        return res
