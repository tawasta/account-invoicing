from odoo import fields, models

from odoo.addons import decimal_precision as dp


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

    purchase_price = fields.Float(
        digits=dp.get_precision("Product Price"),
        string="Cost",
        compute="_compute_purchase_price",
    )

    def _compute_commission_payment_state(self):
        for record in self:
            if not record.commission_payment_id:
                continue

            record.commission_payment_state = record.commission_payment_id.state

    def _compute_purchase_price(self):
        for record in self:
            record.purchase_price = sum(
                record.invoice_line_ids.mapped("purchase_price")
            )
