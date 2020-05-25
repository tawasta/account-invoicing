from odoo import api, models


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        # Handling for when invoicing a down payment
        invoice = super(SaleAdvancePaymentInv, self)._create_invoice(
            order, so_line, amount
        )

        invoice.notice_period = (
            order.partner_id.notice_period or order.company_id.notice_period
        )

        return invoice
