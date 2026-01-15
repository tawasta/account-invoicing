from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    automatic_invoice_print = fields.Boolean(string="Print report on Post", copy=False)

    show_automatic_invoice_print = fields.Boolean(
        compute=lambda self: self._compute_show_automatic_print()
    )

    def _compute_show_automatic_print(self):
        for record in self:
            if record.model == "account.move":
                record.show_automatic_invoice_print = True
            else:
                record.show_automatic_invoice_print = False

    @api.constrains("automatic_invoice_print")
    def check_invoice_print_applicability(self):
        for record in self:
            if record.model != "account.move" and record.automatic_invoice_print:
                raise ValidationError(
                    _("Automatic invoice print is not possible for non-invoices.")
                )
