from odoo import models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def validate_partner_bank_id(self):
        for record in self:
            if record.partner_bank_id:
                if record.type in ('in_invoice', 'out_refund') and \
                        record.partner_bank_id.partner_id != record.partner_id.commercial_partner_id:
                    # Skip the constraint for requiring invoice partner to own the used bank account
                    continue
                else:
                    super().validate_partner_bank_id()
