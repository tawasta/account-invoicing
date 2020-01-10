
from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    salesperson_phone = fields.Char()

    salesperson_email = fields.Char()

    @api.onchange('user_id')
    def user_id_onchange_phone_and_email(self):
        phone, email = (self.user_id.partner_id.phone,
                        self.user_id.partner_id.email)

        if self.salesperson_phone:
            self.comment = self.comment.replace(
                '\n' + self.salesperson_phone, '')
        if self.salesperson_email:
            self.comment = self.comment.replace(
                '\n' + self.salesperson_email, '')

        if self._origin.user_id:
            old_phone, old_email = (self._origin.user_id.partner_id.phone,
                                    self._origin.user_id.partner_id.email)

            self.comment = self._origin.comment.replace(
                '\n' + old_phone, '').replace('\n' + old_email, '')

        if phone:
            self.comment += '\n{}'.format(phone)
        if email:
            self.comment += '\n{}'.format(email)

        self.salesperson_phone = self.user_id.phone
        self.salesperson_email = self.user_id.email
