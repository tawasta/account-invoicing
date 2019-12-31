
from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    salesperson_phone = fields.Char(
        string="Salesperson Phone"
    )

    salesperson_email = fields.Char(
        string="Salesperson Email"
    )

    def remove_words(self, run_lines, words_to_remove=None):
        """Remove Phonenumber and Email from run_lines"""

        # For possible later use
        if words_to_remove is None:
            words_to_remove = []

        if self.salesperson_phone:
            words_to_remove.append(self.salesperson_phone)
        if self.salesperson_email:
            words_to_remove.append(self.salesperson_email)
        new_comment = run_lines
        if words_to_remove:
            run_lines = run_lines.split('\n')
            new_comment = [
                line for line in run_lines if not any(
                    word in line for word in words_to_remove)
            ]
            new_comment = '\n'.join(new_comment)
        return new_comment

    @api.onchange('user_id')
    def user_id_onchange_phone_and_email(self):
        if self.user_id:
            phone, email = (self.user_id.partner_id.phone,
                            self.user_id.partner_id.email)

            # First remove phone and email
            new_comment = self.remove_words(self._origin.comment)
            self.salesperson_phone, self.salesperson_email = phone, email

            # This is needed to remove new values of phone and email
            new_comment = self.remove_words(new_comment)

            # Conditions to add newlines
            email_line = '\n' if new_comment or phone else ''
            phone_line = '\n' if new_comment else ''

            self.comment = "%s%s%s" % (
                '%s' % new_comment if new_comment else '',
                '%s%s' % (phone_line, phone) if phone else '',
                '%s%s' % (email_line, email) if email else ''
            )
