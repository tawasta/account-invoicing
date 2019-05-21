# -*- coding: utf-8 -*-
from odoo import models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    def _onchange_payment_term_date_invoice(self):
        # Override payment term onchange to prefer preset due date

        override_due_date = False

        if self.type == 'in_invoice':
            # Store the due date
            if self.date_due:
                override_due_date = True

            if override_due_date:
                date_due = self.date_due

        # Run the normal onchange
        super(AccountInvoice, self)._onchange_payment_term_date_invoice()

        # Restore the overwritten due date
        if override_due_date:
            self.date_due = date_due
