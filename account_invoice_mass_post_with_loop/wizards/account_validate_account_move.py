from odoo import _
from odoo.exceptions import UserError

from odoo.addons.account.wizard.account_validate_account_move import (
    ValidateAccountMove as ValidateAccountMoveOriginal,
)


def validate_move(self):
    if self._context.get("active_model") == "account.move":
        domain = [
            ("id", "in", self._context.get("active_ids", [])),
            ("state", "=", "draft"),
        ]
    elif self._context.get("active_model") == "account.journal":
        domain = [
            ("journal_id", "=", self._context.get("active_id")),
            ("state", "=", "draft"),
        ]
    else:
        raise UserError(_("Missing 'active_model' in context."))

    moves = self.env["account.move"].search(domain).filtered("line_ids")
    if not moves:
        raise UserError(_("There are no journal items in the draft state to post."))

    for move in moves:
        move._post(not self.force_post)

    return {"type": "ir.actions.act_window_close"}


ValidateAccountMoveOriginal.validate_move = validate_move
