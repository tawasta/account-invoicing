from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    commission_paid = fields.Boolean(
        string="Commission paid", default=False, readonly=True, copy=False
    )

    def action_set_commission_paid(self):
        for record in self:
            record.commission_paid = True
            record.invoice_line_ids.write({"commission_paid": True})
