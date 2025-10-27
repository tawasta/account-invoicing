# -*- coding: utf-8 -*-
import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)

ALLOWED_TYPES = ('in_invoice', 'in_refund', 'in_receipt')
ALLOWED_DISPLAY = ('product', 'line_section', 'line_note')


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    mark_for_delete = fields.Boolean(
        string="Delete line",
        help="Tick to delete this line (draft vendor bills only).",
    )

    def write(self, vals):
        res = super().write(vals)

        if vals.get('mark_for_delete'):
            deletables = self.filtered(
                lambda l: l.move_id
                and l.move_id.state == 'draft'
                and l.move_id.move_type in ALLOWED_TYPES
                and l.display_type in ALLOWED_DISPLAY
            )
            if deletables:
                deletables.unlink()
        return res
