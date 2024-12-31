from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_invoice_line_key_cols(self):
        res = super()._get_invoice_line_key_cols()

        res.append("id")
        res.append("name")

        return res
