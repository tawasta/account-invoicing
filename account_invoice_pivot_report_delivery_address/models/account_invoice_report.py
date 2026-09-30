from odoo import api, fields, models
from odoo.tools import SQL


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    partner_shipping_id = fields.Many2one(
        "res.partner", string="Delivery Address", readonly=True
    )

    _depends = {
        "account.move": ["partner_shipping_id"],
    }

    @api.model
    def _select(self) -> SQL:
        return SQL(
            "%s, move.partner_shipping_id AS partner_shipping_id", super()._select()
        )
