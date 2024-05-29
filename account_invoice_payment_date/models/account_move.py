from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    payment_date = fields.Date(
        string="Payment date",
        copy=False,
        compute="_compute_payment_date",
        store=True,
    )

    def write(self, vals):
        res = super().write(vals)
        if "payment_state" in vals and vals["payment_state"] == "paid":
            self._compute_payment_date()

        return res

    def _compute_payment_date(self):
        for record in self:
            if record.payment_state != "paid":
                record.payment_date = False
                continue

            reconciled_payments = record._get_reconciled_payments()

            if reconciled_payments:
                # Invoice has related payments
                if all(payment.is_matched for payment in reconciled_payments):
                    record.payment_date = max(reconciled_payments.mapped("date"))
                else:
                    record.payment_date = False
            else:
                # Invoice has no related payments,
                # but has been marked as paid with an accounting entry
                payment_date = False
                for (
                    _partial,
                    _amount,
                    counterpart_line,
                ) in record._get_reconciled_invoices_partials():
                    if not payment_date or counterpart_line.date > payment_date:
                        payment_date = counterpart_line.date

                record.payment_date = payment_date

    def _cron_compute_payment_date(self):
        records = self.search(
            [("payment_date", "=", False), ("payment_state", "=", "paid")]
        )
        records._compute_payment_date()
