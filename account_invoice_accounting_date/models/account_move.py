from odoo import api
from odoo import fields
from odoo import models


class AccountMove(models.Model):

    _inherit = "account.move"

    date = fields.Date(string="Accounting date")

    @api.onchange("invoice_date", "highest_name", "company_id")
    def _onchange_invoice_date(self):
        # Save accounting date for a temporary variable to allow setting a different accounting date
        accounting_date = self.date

        res = super()._onchange_invoice_date()

        if (
            accounting_date
            and self.invoice_date
            and accounting_date >= self.invoice_date
        ):
            # Allow auto-change if invoice date is later than accounting date
            self.date = accounting_date
        return res
