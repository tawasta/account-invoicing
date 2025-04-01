from odoo import fields, models


class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"

    is_reconciled = fields.Boolean(
        string="Is Reconciled",
        compute="_compute_is_reconciled",
    )

    def _compute_is_reconciled(self):
        for record in self:
            record.is_reconciled = all(record.line_ids.mapped("is_reconciled"))
