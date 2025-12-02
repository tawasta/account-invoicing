import logging

from odoo import models

_logger = logging.getLogger(__name__)


class AccountMoveReversal(models.TransientModel):
    _inherit = "account.move.reversal"

    def reverse_moves(self, is_modify=False):
        action = super().reverse_moves(is_modify=is_modify)
        origins = self.move_ids.filtered(
            lambda m: m.is_invoice(include_receipts=True)
        ).sorted("id")
        new_moves = self.new_move_ids.filtered(
            lambda m: m.is_invoice(include_receipts=True)
        ).sorted("id")

        if not origins or not new_moves:
            return action

        if len(origins) != len(new_moves):
            _logger.warning(
                "[carryover] count mismatch (origins=%s, new=%s) — "
                "skip carryover to avoid wrong pairing",
                len(origins),
                len(new_moves),
            )
            return action

        for origin, new in zip(origins, new_moves, strict=False):
            vals = {}
            if origin.ref:
                vals["ref"] = origin.ref or False

            vals["invoice_user_id"] = origin.invoice_user_id.id or False
            new.write(vals)
        return action
