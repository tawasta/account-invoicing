from odoo import _, models
from odoo.exceptions import ValidationError


class AccountMove(models.Model):

    _inherit = "account.move"

    def _post(self, soft=True):
        """
        Run all the checks for required fields. If any errors, show all of them
        to user and prevent confirming the invoice until they are fixed.
        """
        ir_config_model = self.env["ir.config_parameter"]

        errors = []

        for record in self:

            # Check for partner address data
            if ir_config_model.sudo().get_param(
                "account_move_confirmation.partner_address_required"
            ):
                partner = record.partner_id
                if (
                    not partner
                    or not partner.street
                    or not partner.zip
                    or not partner.city
                    or not partner.country_id
                ):
                    errors.append(
                        _(
                            "- Invoice '%s': Address information missing for "
                            "Partner %s (ID %s)",
                            record.name,
                            partner.name,
                            partner.id,
                        )
                    )

            # Check for partner email
            if ir_config_model.sudo().get_param(
                "account_move_confirmation.partner_email_required"
            ):
                partner = record.partner_id
                if not partner or not partner.email:
                    errors.append(
                        _(
                            "- Invoice '%s': E-mail address missing for Partner %s (ID %s)",
                            record.name,
                            partner.name,
                            partner.id,
                        )
                    )

            # Check for shipping address' address data
            if ir_config_model.sudo().get_param(
                "account_move_confirmation.partner_shipping_address_required"
            ):
                partner = record.partner_shipping_id
                if (
                    not partner
                    or not partner.street
                    or not partner.zip
                    or not partner.city
                    or not partner.country_id
                ):
                    errors.append(
                        _(
                            "- Invoice '%s': Address information missing for Delivery "
                            "Address %s (ID %s)",
                            record.name,
                            partner.name,
                            partner.id,
                        )
                    )

        if errors:
            msg = _("Please fix the following data before confirming the invoice(s):\n")
            raise ValidationError(msg + "\n".join(errors))

        # If no missing data, proceed with confirming
        return super()._post(soft=soft)
