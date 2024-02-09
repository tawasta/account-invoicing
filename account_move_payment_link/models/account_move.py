from odoo import api, fields, models
import logging

class AccountMove(models.Model):
    _inherit = "account.move"

    link = fields.Char(string="Payment Link", compute="_compute_payment_link")

    @api.depends("amount_total", "partner_id")
    def _compute_payment_link(self):
        payment_link_wizard = self.env["payment.link.wizard"]
        for rec in self:
            logging.info("======REC ARVO====");
            logging.info(rec);
            temp_wizard = payment_link_wizard.create(
                {
                    "res_model": "sale.order",
                    "res_id": rec.id,
                    "amount": rec.amount_total,
                    "partner_id": rec.partner_id.id,
                    "currency_id": rec.currency_id.id,
                    "description": rec.payment_reference,
                }
            )
            temp_wizard._compute_values()
            rec.link = temp_wizard.link
