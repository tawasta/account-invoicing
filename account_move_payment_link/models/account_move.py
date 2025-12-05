import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = "account.move"

    payment_link = fields.Char(
        copy=False,
        help="Payment link to be sent to the customer.",
    )

    def _post(self, soft=True):
        res = super()._post(soft=soft)

        for record in self.filtered(lambda r: r.is_sale_document()):
            record._create_payment_link()

        return res

    def _create_payment_link(self):
        self.ensure_one()
        if not self.is_sale_document():
            return False

        _logger.debug("Creating payment link for invoice ID %s", self.id)

        payment_link_wizard = self.env["payment.link.wizard"]

        wizard_vals = {
            "res_model": "account.move",
            "res_id": self.id,
            "amount": self.amount_total,
            "partner_id": self.partner_id.id,
            "currency_id": self.currency_id.id,
        }

        try:
            temp_wizard = payment_link_wizard.with_context(
                active_model="account.move"
            ).create(wizard_vals)
            self.payment_link = temp_wizard.link
        except Exception as e:
            _logger.error(
                "Failed to create payment link for invoice ID %s: %s", self.id, str(e)
            )
            return False

        return True
