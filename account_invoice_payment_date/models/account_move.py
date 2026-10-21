from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    payment_date = fields.Date(
        string="Payment date",
        copy=False,
        compute="_compute_payment_date",
        store=True,
    )

    @api.depends("amount_residual", "move_type", "state", "company_id")
    def _compute_payment_state(self):
        res = super()._compute_payment_state()

        for move in self:
            move._compute_payment_date()

        # This function does not really return anything (usually)
        return res

    def _compute_payment_date(self):
        for record in self:
            if record.payment_state != "paid":
                record.payment_date = False
                continue

            reconciled_payments = record._get_reconciled_payments()
            reconciled_partial_payments = record._get_reconciled_invoices_partials()

            if reconciled_payments:
                # Invoice has related payments
                if all(payment.is_matched for payment in reconciled_payments):
                    record.payment_date = max(reconciled_payments.mapped("date"))
                else:
                    record.payment_date = False
            elif reconciled_partial_payments:
                # Invoice has no related payments,
                # but has been marked as paid with an accounting entry
                payment_date = False
                for (
                    _partial,
                    _amount,
                    counterpart_line,
                ) in reconciled_partial_payments[0]:
                    if not payment_date or counterpart_line.date > payment_date:
                        payment_date = counterpart_line.date

                record.payment_date = payment_date
            else:
                record.payment_date = record.payment_date or False

    def _cron_compute_payment_date(self):
        records = self.search(
            [("payment_date", "=", False), ("payment_state", "=", "paid")]
        )
        records._compute_payment_date()
