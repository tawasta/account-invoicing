from odoo import api, models


class AccountMoveLine(models.Model):

    _inherit = "account.move.line"

    # Note that this decorator is needed!
    @api.model_create_multi
    def create(self, vals_list):

        for vals in vals_list:
            # We are only interested in lines which have a product
            product_id = vals.get("product_id", False)
            # Just in case
            move_id = vals.get("move_id", False)

            if product_id and move_id:
                # Get expense/income account from partner, if applicable
                account = self.get_invoice_line_partner_account(
                    move_id, product_id, True
                )
                if account:
                    vals["account_id"] = account.id

        return super().create(vals_list)

    @api.onchange("product_id")
    def _onchange_product_id(self):
        res = super()._onchange_product_id()
        for record in self:
            if not record.move_id.partner_id:
                continue

            move = record.move_id
            product = record.product_id

            account = record.get_invoice_line_partner_account(move, product, False)
            if account:
                record.account_id = account.id

        return res

    def get_invoice_line_partner_account(self, move, product, create):
        res = False

        # Avoids new_id problem if onchange-method is used
        if create:
            move = self.env["account.move"].search([("id", "=", move)])
            product = self.env["product.product"].search([("id", "=", product)])

        if (
            move.move_type in ("out_invoice", "out_refund")
            and move.partner_id.property_account_income_id
            and not product.property_account_income_id
        ):
            res = move.partner_id.property_account_income_id

        elif (
            move.move_type in ("in_invoice", "in_refund")
            and move.partner_id.property_account_expense_id
            and not product.property_account_expense_id
        ):
            res = move.partner_id.property_account_expense_id

        return res
