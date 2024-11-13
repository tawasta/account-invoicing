import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):

    _inherit = "account.move"

    payment_link = fields.Char(
        string="Payment Link",
        copy=False,
        help="Payment link to be sent to the customer.",
    )

    def _post(self, soft=True):
        res = super()._post(soft=soft)

        payment_link_wizard = self.env["payment.link.wizard"]
        ctx = {"active_model": "account.move"}

        for record in self.filtered(lambda r: r.is_sale_document()):

            _logger.debug("Creating payment link for invoice ID %s", record.id)

            temp_wizard = payment_link_wizard.with_context(ctx).create(
                {
                    "res_model": "account.move",
                    "res_id": record.id,
                    "amount": record.amount_total,
                    "partner_id": record.partner_id.id,
                    "currency_id": record.currency_id.id,
                }
            )

            temp_wizard._compute_link()
            record.payment_link = temp_wizard.link

        return res
