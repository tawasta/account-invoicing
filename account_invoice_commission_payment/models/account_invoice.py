from odoo import fields
from odoo import models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    commission_payment_id = fields.Many2one(
        "account.payment", string="Commission payment"
    )

    commission_payment_state = fields.Char(
        string="Commission",
        help="Commission payment state",
        compute="_compute_commission_payment_state",
    )

    def _compute_commission_payment_state(self):
        for record in self:
            if not record.commission_payment_id:
                continue

            record.commission_payment_state = record.commission_payment_id.state
