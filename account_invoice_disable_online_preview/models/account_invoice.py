from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def get_access_action(self, access_uid=None):
        # Disable online access
        return False
