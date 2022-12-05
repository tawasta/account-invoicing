from odoo import _, api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.move"

    salesperson_email = fields.Char()

    @api.onchange("user_id")
    def user_id_onchange_phone_and_email(self):
        email = self.user_id.partner_id.email or ""

        self.narration = self.narration or ""

        if self.salesperson_email:
            self.narration = self.narration.replace(
                "\n" + _("Handler: ") + self.salesperson_email, ""
            ).replace(_("Handler: ") + self.salesperson_email, "")

        email_line = "\n" if self.narration else ""

        if email:
            self.narration += "{}{}{}".format(email_line, _("Handler: "), email)

        self.salesperson_email = self.user_id.partner_id.email
