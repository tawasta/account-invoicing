from odoo import _, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _compute_amount(self):
        """
        Check if there is a need for updating picking priorities.
        We are using _compute_amount instead of _get_invoice_in_payment_state
        as the latter doesn't yet save the new state, so the has_open_invoices()-method
        on pickings would give an incorrect result
        """
        res = super()._compute_amount()

        priority = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("stock.picking.completed.payment.priority")
        )

        for record in self:
            pickings = record.stock_picking_ids
            if record.payment_state != "paid" or not pickings:
                # Nothing to do
                continue

            record.message_post(
                body=_("Changing priority for pickings: {}").format(
                    pickings.mapped("name")
                )
            )
            priority_msg = _(
                "Priority changed when invoice {} was marked as paid".format(
                    record.name
                )
            )
            for picking in pickings:
                if not picking.has_open_invoices() and record.move_type != "out_refund":
                    # When all the invoices for a picking are paid, change the picking priority
                    picking.message_post(body=priority_msg)
                    picking.sudo().write({"priority": priority})

        return res
