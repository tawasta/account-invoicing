from odoo import api, models


class AccountMoveLine(models.Model):

    _inherit = "account.move.line"

    @api.model
    def create(self, vals):
        res = super().create(vals)

        if not vals.get("sequence"):
            # TODO: a better way to decide if the line is done from UI or programmatically
            # Get expense/income account from partner, if applicable
            account = res.get_invoice_line_partner_account()
            if account:
                res.account_id = account.id

        return res

    @api.onchange("product_id")
    def _onchange_product_id(self):
        res = super()._onchange_product_id()

        for record in self:
            if not record.move_id.partner_id:
                continue

            account = record.get_invoice_line_partner_account()
            if account:
                record.account_id = account.id

        return res

    def get_invoice_line_partner_account(self):
        self.ensure_one()
        res = False

        if (
            self.move_id.move_type in ("out_invoice", "out_refund")
            and self.move_id.partner_id.property_account_income_id
            and not self.product_id.property_account_income_id
        ):
            res = self.move_id.partner_id.property_account_income_id

        elif (
            self.move_id.move_type in ("in_invoice", "in_refund")
            and self.move_id.partner_id.property_account_expense_id
            and not self.product_id.property_account_expense_id
        ):
            res = self.move_id.partner_id.property_account_expense_id

        return res
