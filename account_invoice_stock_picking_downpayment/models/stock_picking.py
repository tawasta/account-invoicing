from odoo import _, models
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        for record in self:
            if record.has_open_invoices():
                # Don't allow validating pickings if they have open invoices
                raise ValidationError(
                    _(
                        "You cannot confirm the transfer because some of the invoices "
                        "are still pending"
                    )
                )

        return super().button_validate()

    def has_open_invoices(self):
        self.ensure_one()
        # Only check lines with policy "Invoice delivered"
        so_lines_to_deliver = self.sudo().sale_id.order_line.filtered(
            lambda r: r.product_id.invoice_policy == "delivery"
        )
        states = so_lines_to_deliver.mapped("order_id.invoice_ids.payment_state")
        is_open = "not_paid" in states or "in_payment" in states or "partial" in states

        return is_open
