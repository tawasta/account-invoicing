from odoo import models


class AccountPayment(models.Model):

    _inherit = "account.payment"

    def action_commission_send(self):
        self.ensure_one()
        mail_template = self.env.ref(
            "account_payment_commission_send_email.email_template_commission_payment",
            raise_if_not_found=False,
        )

        if mail_template and mail_template.lang:
            lang = mail_template._render_lang(self.ids)[self.id]

        ctx = {
            "default_model": "account.payment",
            "default_res_ids": self.ids,
            "default_template_id": mail_template.id if mail_template else None,
            "default_composition_mode": "comment",
            "default_email_layout_xmlid": "mail.mail_notification_layout",
            "force_email": True,
            "model_description": self.with_context(lang=lang).type_name,
        }

        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "mail.compose.message",
            "views": [(False, "form")],
            "view_id": False,
            "target": "new",
            "context": ctx,
        }
