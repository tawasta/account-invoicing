from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def action_post(self):
        """Print automatically reports related to an invoice"""
        res = super().action_post()

        report_actions = []
        reports = self.env["ir.actions.report"].search(
            [("automatic_invoice_print", "=", True)]
        )

        if reports and self:
            for report in reports:
                report_actions.append(report.report_action(self))

            return {
                "type": "ir.actions.client",
                "tag": "do_multi_print",
                "params": {
                    "reports": report_actions,
                },
            }
        return res
