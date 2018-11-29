# -*- coding: utf-8 -*-
from odoo import api, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.model
    def _refund_cleanup_lines(self, lines):
        res = super(AccountInvoice, self)._refund_cleanup_lines(lines)

        for line_index, line in enumerate(lines):
            # TODO: can we use isinstance?
            if not line._name == 'account.invoice.line':
                continue

            # Inject analytic tag ids into the tuple
            if line.analytic_tag_ids:
                values = res[line_index][2]
                values['analytic_tag_ids'] = \
                    [(6, 0, line.analytic_tag_ids.ids)]

                res[line_index] = (0, 0, values)

        return res
