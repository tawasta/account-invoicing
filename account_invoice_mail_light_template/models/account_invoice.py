from odoo import api
from odoo import models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.multi
    def _send_email(self):
        self = self.with_context(custom_layout='mail.mail_notification_light')
        return super(AccountInvoice, self)._send_email()
