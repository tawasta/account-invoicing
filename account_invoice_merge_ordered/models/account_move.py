from collections import OrderedDict

from odoo import api, models


class AccountMove(models.Model):

    _inherit = "account.move"

    @api.model
    def _get_first_invoice_fields(self, invoice):

        res = super()._get_first_invoice_fields(invoice=invoice)

        res["invoice_line_ids"] = OrderedDict()

        return res
