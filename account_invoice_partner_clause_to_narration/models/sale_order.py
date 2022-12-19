from odoo import models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()

        if self.partner_id and self.partner_id.invoice_clause:

            if invoice_vals.get("narration"):
                invoice_vals["narration"] += "{}{}".format(
                    "\n", self.partner_id.invoice_clause.clause
                )
            else:
                invoice_vals["narration"] += "{}".format(
                    self.partner_id.invoice_clause.clause
                )

        return invoice_vals
