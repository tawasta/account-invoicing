from odoo import api, fields, models


class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"

    manual_input = fields.Boolean(default=False, help="Manually input bank statement")
    manual_date = fields.Date(help="Manually override statement date")

    @api.onchange("line_ids")
    def _compute_manual_balance(self):
        for stmt in self:
            if stmt.manual_input and stmt.balance_start == 0:
                stmt._compute_balance_start()

    @api.depends("manual_date", "line_ids.internal_index", "line_ids.state")
    def _compute_date_index(self):
        res = super()._compute_date_index()
        for stmt in self:
            if stmt.manual_date:
                stmt.date = stmt.manual_date

        return res
