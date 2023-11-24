from odoo import _, models
from odoo.exceptions import UserError


class AccountUpdateLockDate(models.TransientModel):

    _inherit = "account.update.lock_date"

    def _check_execute_allowed(self):
        self.ensure_one()
        has_locking_group = self.env.user.has_group(
            "account_lock_date_update_group.account_date_lock_group"
        )
        if not (has_locking_group or self.env.user._is_admin()):
            raise UserError(_("You are not allowed to execute this action."))
