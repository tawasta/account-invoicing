from odoo import _, fields, models


class AccountInvoiceCommissionPaymentWizard(models.TransientModel):
    _inherit = "account.invoice.commission.payment.wizard"

    batch_name = fields.Char(
        string="Batch name",
        help="This information will be used to distinguish this batch of invoices",
        required=True,
        default=lambda self: self._get_default_batch_name(),
    )

    def _get_default_batch_name(self):
        batch_name = _(
            "{}: commission payments {}".format(
                self.env.user.display_name, fields.Datetime.now().isoformat()
            )
        )
        return batch_name

    def create_commission_payments(self, invoice_ids):
        # Override creating commission payments and use queue
        batch = self.env["queue.job.batch"].sudo().get_new_batch(self.batch_name)

        for invoice in invoice_ids:
            job_desc = _(
                "Creating commission payment for invoice '{}'".format(
                    invoice.display_name
                )
            )
            self.with_context(job_batch=batch).with_delay(
                description=job_desc
            ).create_commission_payment(invoice)

        batch.sudo().enqueue()
        batch.sudo().message_subscribe(self.env.user.partner_id.ids)

    def create_commission_payment(self, invoice):
        res = super().create_commission_payment(invoice)

        return res
