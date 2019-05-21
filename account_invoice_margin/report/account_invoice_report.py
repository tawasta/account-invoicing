# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    margin = fields.Float(
        string='Total margin',
        readonly=True,
    )

    def _select(self):
        select_str = super(AccountInvoiceReport, self)._select()

        # Hackish, but works without overwriting anything
        select_str = select_str.replace(
            'sub.price_total as price_total',
            'sub.price_total as price_total, sub.margin as margin'
        )

        return select_str

    def _sub_select(self):
        select_str = super(AccountInvoiceReport, self)._sub_select()

        select_str += ',SUM(ail.margin * invoice_type.sign_qty) AS margin'

        return select_str
