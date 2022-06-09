from odoo import api, models


class AccountInvoiceSend(models.TransientModel):

    _inherit = "account.invoice.send"

    @api.multi
    def _send_email(self):
        self = self.with_context(custom_layout="mail.mail_notification_light")
        return super(AccountInvoiceSend, self)._send_email()
