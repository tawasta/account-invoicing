from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _compute_narration(self):
        # Disable narration compute
        for record in self:
            if not record.narration:
                super(AccountMove, record)._compute_narration()
            else:
                continue
