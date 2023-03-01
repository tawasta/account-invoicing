from odoo import models


class AccountMove(models.Model):

    _inherit = "account.move"

    def action_reverse(self):
        action = super().action_reverse()

        if self.is_invoice():
            action["date_delivered"] = self.date_delivered
            action["header_text"] = self.header_text

        return action
