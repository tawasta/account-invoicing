from odoo import api
from odoo import models
from odoo import _
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):

    _inherit = "account.move"

    @api.constrains("name", "journal_id", "state")
    def _check_unique_sequence_number(self):
        try:
            super()._check_unique_sequence_number()
        except ValidationError as e:
            _logger.warning(
                _("Allowing an overlapping invoice sequence for invoice {}!").format(
                    self.name
                )
            )
            _logger.warning(e)
