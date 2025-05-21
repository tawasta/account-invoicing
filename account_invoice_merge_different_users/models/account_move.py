import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    # 1. Private attributes
    _inherit = "account.move"

    # 7. Action methods
    @api.model
    def _get_invoice_key_cols(self):
        """Remove user check when merging invoices"""
        res = super()._get_invoice_key_cols()
        if "user_id" in res:
            res.remove("user_id")
            _logger.debug("User check for invoice merging bypassed.")
        return res
