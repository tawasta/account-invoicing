import logging

from odoo import _, api, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):

    _inherit = "account.move"

    @api.constrains("name", "journal_id", "state")
    def _check_unique_sequence_number(self):
        try:
            super()._check_unique_sequence_number()
        except ValidationError as e:
            _logger.warning(
                _("Allowing an overlapping invoice sequence for invoices {}!").format(
                    self.ids
                )
            )
            _logger.warning(e)
