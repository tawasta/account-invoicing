from odoo import api, models


class AccountInvoice(models.Model):

    _inherit = "account.move"

    @api.onchange("invoice_date", "highest_name", "company_id")
    def _onchange_invoice_date(self):
        # Override payment term onchange to prefer preset due date
        override_due_date = False

        if self.move_type == "in_invoice":  # was self.type
            # Store the due date
            if self.invoice_date_due:  # was self.due_date
                override_due_date = True
            if override_due_date:
                date_due = self.invoice_date_due  # was self.due_date

        # Run the normal onchange
        super(
            AccountInvoice, self
        )._onchange_invoice_date()  # was _onchange_payment_term_date_invoice()

        # Restore the overwritten due date
        if override_due_date:
            self.invoice_date_due = date_due
