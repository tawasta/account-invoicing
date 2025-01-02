from odoo import _, fields, models
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"

    # 7. Action methods
    def _post(self, soft=True):
        """Post/Validate the documents."""
        if soft:
            future_moves = self.filtered(
                lambda move: move.date > fields.Date.context_today(self)
            )
            to_post = self - future_moves
        else:
            to_post = self
        self._check_invoice_payment_term(to_post)
        return super(AccountMove, self)._post(soft)

    # 8. Business methods
    def _check_invoice_payment_term(self, to_post):
        for record in to_post:
            if record.move_type == "out_invoice" and not record.invoice_payment_term_id:
                raise UserError(_("Please set a payment term before validating."))
