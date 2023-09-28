from odoo import _, models
from odoo.exceptions import UserError


class AccountMove(models.Model):

    _inherit = "account.move"

    def action_invoice_approve(self):
        if not all(line.analytic_account_id for line in self.invoice_line_ids):
            msg = _("Please add analytic accounts to all lines before approving")
            raise UserError(msg)

        return super().action_invoice_approve()
