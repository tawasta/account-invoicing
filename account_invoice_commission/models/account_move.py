from odoo import _, api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    commission_paid = fields.Boolean(
        string="Commission processed",
        default=False,
        readonly=True,
        copy=False,
        compute="_compute_commission_paid",
        store=True,
    )

    def action_set_commission_paid(self):
        for record in self:
            record.commission_paid = True
            record.invoice_line_ids.write({"commission_paid": True})

            record.message_post(body=_("Commission set as paid"))

    def action_set_commission_unpaid(self):
        for record in self:
            record.commission_paid = False
            record.invoice_line_ids.write({"commission_paid": False})

            record.message_post(body=_("Commission set as unpaid"))

    @api.depends("invoice_line_ids.commission_paid")
    def _compute_commission_paid(self):
        for record in self:
            if False not in record.invoice_line_ids.mapped("commission_paid"):
                record.commission_paid = True
            else:
                record.commission_paid = False

    def _get_commission_paid(self):
        # For legacy support
        self._compute_commission_paid()
