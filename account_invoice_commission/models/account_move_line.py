from odoo import api
from odoo import fields
from odoo import models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    commission_paid = fields.Boolean(
        string="Commission paid",
        default=False,
        copy=False,
        readonly=True,
    )

    @api.depends("commission_paid")
    def onchange_commission_paid(self):
        for record in self:
            record.move_id._get_commission_paid()
