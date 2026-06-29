from odoo import _, api, models


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    @api.model_create_multi
    def create(self, vals_list):
        auto_trust = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(
                "res_partner_bank_auto_allow_out_payment.auto_allow_out_payment",
                "False",
            )
            == "True"
        )

        if auto_trust:
            for vals in vals_list:
                vals["allow_out_payment"] = True

        records = super().create(vals_list)

        if auto_trust:
            for bank in records:
                if bank.allow_out_payment:
                    acc_number = bank.acc_number or ""
                    acc_ending = acc_number[-4:] if len(acc_number) >= 4 else acc_number
                    if not acc_ending:
                        acc_ending = _("unknown")

                    bank.message_post(
                        body=_(
                            "Bank account ending in %s was created and"
                            " automatically marked as Trusted.",
                            acc_ending,
                        )
                    )

        return records
