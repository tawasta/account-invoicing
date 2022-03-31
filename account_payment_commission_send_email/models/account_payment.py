from odoo import fields, models


class AccountPayment(models.Model):

    _inherit = "account.payment"

    def action_commission_send(self):
        self.ensure_one()
        template = self.env.ref(
            "account_payment_commission_send_email.email_template_commission_payment",
            raise_if_not_found=False,
        )

        local_context = dict(
            self.env.context,
            default_account_payment_id=self.id,
            default_use_template=bool(template),
            default_template_id=template and template.id or False,
        )
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "account.payment.email",
            "target": "new",
            "context": local_context,
        }
