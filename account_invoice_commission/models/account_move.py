from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    commission_paid = fields.Boolean(
        string="Commission paid", default=False, readonly=True, copy=False
    )

    def action_set_commission_paid(self):
        for record in self:
            record.commission_paid = True
            record.invoice_line_ids.write({"commission_paid": True})

    @api.depends("invoice_line_ids.commission_paid")
    def _get_commission_paid(self):
        for record in self:
            if False not in record.invoice_line_ids.mapped("commission_paid"):
                record.commission_paid = True
            else:
                record.commission_paid = False
