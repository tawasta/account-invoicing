from odoo import _, api, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.model
    def create(self, values):
        if values.get("description") is False:
            values["description"] = ""

        if "origin" in values:
            values["description"] = "{}\n{}".format(
                values.get("description", ""), _("Origin: {}").format(values["origin"])
            )

        return super(AccountInvoice, self).create(values)
