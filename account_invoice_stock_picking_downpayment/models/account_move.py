from odoo import _, models


class AccountMove(models.Model):
    _name = "account.move"
    _inherit = ["account.move", "mail.thread"]

    def _compute_payment_state(self):
        """
        Check if there is a need for updating picking priorities.
        We are using _compute_payment_state to check the new state.
        This way has_open_invoices()-method works properly.
        """
        res = super()._compute_payment_state()

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

            record._origin.message_post(
                body=_("Changing priority for pickings: {}").format(
                    pickings.mapped("name")
                )
            )
            priority_msg = _(
                f"Priority changed when invoice {record.name} was marked as paid"
            )
            for picking in pickings:
                if not picking.has_open_invoices() and record.move_type != "out_refund":
                    # When all the invoices for a picking are paid, change the picking priority
                    picking._origin.message_post(body=priority_msg)
                    picking.sudo().write({"priority": priority})

        return res
