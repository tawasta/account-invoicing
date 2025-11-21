from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _compute_narration(self):
        # Only compute narration for records that have no narration
        res = None
        to_compute = self.filtered(lambda m: not m.narration)
        if to_compute:
            res = super(AccountMove, to_compute)._compute_narration()

        return res
