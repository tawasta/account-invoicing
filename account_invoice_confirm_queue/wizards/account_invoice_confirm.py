from odoo import api
from odoo import models
from odoo import _
from odoo.exceptions import UserError


class AccountInvoiceConfirm(models.TransientModel):

    _inherit = "account.invoice.confirm"

    @api.multi
    def invoice_confirm(self):
        context = dict(self._context or {})
        active_ids = context.get("active_ids", []) or []

        if len(active_ids) <= 1:
            # Confirm one invoice immediately
            return super().invoice_confirm()

        # Confirm larger batches as jobs
        invoice_list = (
            self.env["account.invoice"]
            .browse(active_ids)
            .sorted(lambda i: (i.date_invoice, i.reference or "", i.id))
        )

        for record in invoice_list:
            if record.state != "draft":
                raise UserError(
                    _(
                        "Selected invoice(s) cannot be confirmed as they are not in 'Draft' state."
                    )
                )
            job_desc = _("Confirm invoice '{}'".format(record.id))
            record.with_delay(description=job_desc).action_invoice_open_queued()

        return {"type": "ir.actions.act_window_close"}
