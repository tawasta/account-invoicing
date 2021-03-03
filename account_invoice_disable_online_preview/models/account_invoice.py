from odoo import models, api


class AccountInvoice(models.Model):
    @api.multi
    def get_access_action(self, access_uid=None):
        # Disable online access
        return False
