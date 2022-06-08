from odoo import api, fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    notice_period = fields.Integer(
        string="Notice period (days)",
        help="Default notice period (days) for new customers and invoices",
    )

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        self.notice_period = (
            self.partner_id.notice_period or self.company_id.notice_period
        )
