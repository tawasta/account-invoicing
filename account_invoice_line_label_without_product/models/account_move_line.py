from odoo import models


class AccountMoveLine(models.Model):

    _inherit = "account.move.line"

    def _get_computed_name(self):
        res = super()._get_computed_name()
        # Replace product display name from line name
        res = res.replace(self.product_id.display_name, "")

        if not res:
            # Empty name is not allowed
            res = " "

        return res
