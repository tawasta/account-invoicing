import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

ALLOWED_TYPES = {"in_invoice", "in_refund", "in_receipt"}
ALLOWED_DISPLAY = {"product", "line_section", "line_note"}


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    mark_for_delete = fields.Boolean(
        string="Delete line",
        help="Tick to delete this line (draft vendor bills only).",
    )

    def _eligible_for_manual_delete(self):
        """Return only draft vendor bill lines that can be safely deleted."""
        return self.filtered(
            lambda li: (
                li.move_id
                and li.move_id.state == "draft"
                and li.move_id.move_type in ALLOWED_TYPES
                and li.display_type in ALLOWED_DISPLAY
                and li in li.move_id.invoice_line_ids
            )
        )

    def write(self, vals):
        res = super().write(vals)
        if vals.get("mark_for_delete"):
            deletables = self._eligible_for_manual_delete()
            if deletables:
                deletables.unlink()
        return res
