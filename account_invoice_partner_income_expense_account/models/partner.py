from odoo import fields, models


class Partner(models.Model):

    _inherit = "res.partner"

    property_account_income_id = fields.Many2one(
        "account.account",
        company_dependent=True,
        string="Income account",
        oldname="default_income_account",
        domain="[('deprecated', '=', False)]",
        help="This account will be used instead of the default one as "
        "the income account for the current partner",
    )

    property_account_expense_id = fields.Many2one(
        "account.account",
        company_dependent=True,
        string="Expense account",
        oldname="default_expense_account",
        domain="[('deprecated', '=', False)]",
        help="This account will be used instead of the default one as "
        "the expense account for the current partner",
    )
