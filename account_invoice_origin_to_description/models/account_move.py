from odoo import _, api, models


class AccountMove(models.Model):

    _inherit = "account.move"

    @api.model
    def create(self, values):
        if values.get("description") is False:
            values["description"] = ""

        if "invoice_origin" in values:
            values["description"] = "{}\n{}".format(
                values.get("description", ""),
                _("Origin: {}").format(values["invoice_origin"]),
            )

        return super(AccountMove, self).create(values)
