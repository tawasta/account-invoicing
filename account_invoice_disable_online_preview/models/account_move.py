from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def get_access_action(self, access_uid=None):
        # Disable online access
        return False
