from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends("bank_partner_id")
    def _compute_partner_bank_id(self):
        for record in self:
            record.partner_bank_id = False
