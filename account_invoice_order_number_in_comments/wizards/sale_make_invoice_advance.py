from odoo import _, api, models


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        # Handling for when invoicing a down payment
        invoice = super(SaleAdvancePaymentInv, self)._create_invoice(
            order, so_line, amount
        )

        invoice.comment = "{}{}: {}".format(
            invoice.comment and (invoice.comment + "\n") or "",
            _("Our Order Reference"),
            order.name,
        )

        return invoice
