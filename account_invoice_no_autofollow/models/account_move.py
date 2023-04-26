from odoo import models


class AccountMove(models.Model):

    _inherit = "account.move"

    def _post(self, soft=True):
        res = super()._post()
        for record in self:
            # We can't prevent the subscription, so we'll just
            # unsubscribe right after the confirmation
            if record.partner_id in record.message_partner_ids:
                record.message_unsubscribe([record.partner_id.id])
        return res
