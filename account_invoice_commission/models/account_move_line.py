from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    commission_paid = fields.Boolean(
        string="Commission processed",
        default=False,
        copy=False,
        readonly=True,
    )

    @api.depends("commission_paid")
    def onchange_commission_paid(self):
        for record in self:
            record.move_id._compute_commission_paid()
