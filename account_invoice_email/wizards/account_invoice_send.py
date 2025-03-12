from email_validator import EmailNotValidError, validate_email

from odoo import _, models
from odoo.exceptions import ValidationError


class AccountMoveSend(models.TransientModel):
    _inherit = "account.move.send"

    def action_send_and_print(
        self, force_synchronous=False, allow_fallback_pdf=False, **kwargs
    ):
        for invoice in self.move_ids:
            partner = invoice.partner_id
            if not partner.invoice_email:
                raise ValidationError(
                    _("Partner '{}' has no invoice email address").format(partner.name)
                )

            try:
                validate_email(partner.invoice_email)
            except EmailNotValidError as err:
                raise ValidationError(
                    _("Partner '{}' invoice email address '{}' is not valid").format(
                        partner.name, partner.invoice_email
                    )
                ) from err

        return super().action_send_and_print(
            force_synchronous=force_synchronous,
            allow_fallback_pdf=allow_fallback_pdf,
            **kwargs,
        )
