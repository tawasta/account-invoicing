from odoo import models
from odoo import _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def action_invoice_open(self):
        for record in self:
            if not record.partner_bank_id:
                raise UserError(_("Please set bank account before validating"))

        super().action_invoice_open()

    def _get_default_bank_id(self, type, company_id):
        # Disable automated bank account selection
        return False
