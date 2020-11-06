from odoo import _
from odoo import fields
from odoo.exceptions import UserError
from odoo import models


class AccountInvoiceMassRefund(models.TransientModel):
    _name = "account.invoice.mass.refund"

    unreconcile = fields.Boolean(string="Unreconcile before refunding")
    description = fields.Char(string="Description for refunds", required=True,)
    filter_refund = fields.Selection(
        [
            ("refund", "Create a draft credit note"),
            ("cancel", "Cancel: create credit note and reconcile"),
            (
                "modify",
                "Modify: create credit note, reconcile and create a new draft invoice",
            ),
        ],
        default="refund",
        string="Credit Method",
        required=True,
        help="Choose how you want to credit this invoice. You cannot Modify and Cancel if the invoice is already reconciled",
    )

    def get_cancellable_states(self):
        return ["open", "paid"]

    def confirm(self):

        records = self.env["account.invoice"].browse(self._context.get("active_ids"))
        account_invoice_refund = self.env["account.invoice.refund"]

        allowed_states = self.get_cancellable_states()

        if any(r.state not in allowed_states for r in records):
            msg = _("Please only select invoices that are in open or paid state")
            raise UserError(msg)

        for record in records:
            if self.unreconcile and record.move_id:
                # Unreconcile entries
                aml_model = self.env["account.move.line"]

                reconcile_view = record.move_id.open_reconcile_view()
                domain = reconcile_view.get("domain")

                for aml in aml_model.search(domain):
                    aml.remove_move_reconcile()

        refund = account_invoice_refund.create({"description": self.description})

        # Create draft refunds
        refund.compute_refund(self.filter_refund)
