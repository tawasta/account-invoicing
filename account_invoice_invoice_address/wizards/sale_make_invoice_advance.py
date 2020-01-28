from odoo import api, models


class SaleAdvancePaymentInv(models.TransientModel):

    # 1. Private attributes
    _inherit = "sale.advance.payment.inv"

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.multi
    def _create_invoice(self, order, so_line, amount):
        # Handling for when invoicing a down payment
        invoice = super(SaleAdvancePaymentInv, self)._create_invoice(
            order, so_line, amount
        )
        invoice.partner_id = order.partner_id.id
        invoice.partner_invoice_id = order.partner_invoice_id.id
        return invoice
