from odoo import models


class AccountMove(models.Model):

    _inherit = "account.move"

    def action_mass_post(self):
        # Post multiple invoices at once
        records = self.filtered(lambda r: r.state == "draft")
        records.action_post()
