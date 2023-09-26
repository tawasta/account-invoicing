from odoo import api, models


class AccountMove(models.Model):

    _inherit = "account.move"

    @api.model
    def _get_invoice_line_key_cols(self):
        fields = super()._get_invoice_line_key_cols()
        fields.append("analytic_tag_ids")
        return fields
