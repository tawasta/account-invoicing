from odoo import _, models
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"

    def action_post(self):
        for record in self:
            if record.move_type == "out_invoice" and not record.partner_bank_id:
                raise UserError(_("Please set a bank account before posting"))

        return super().action_post()
