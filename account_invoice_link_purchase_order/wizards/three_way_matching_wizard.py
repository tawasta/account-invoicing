import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ThreeWayMatchingWizard(models.TransientModel):
    _name = "three.way.matching.wizard"
    _description = "Match purchase orders to invoice"

    invoice_id = fields.Many2one("account.move", string="Vendor Bill", required=True)
    purchase_order_id = fields.Many2one(
        "purchase.order", string="Purchase Order", required=True
    )
    wizard_line_ids = fields.One2many(
        comodel_name="three.way.matching.wizard.line", inverse_name="wizard_id"
    )

    @api.onchange("purchase_order_id", "invoice_id")
    def _compute_wizard_line_ids(self):
        self.ensure_one()
        po_line = self.env["purchase.order.line"].sudo()
        invoice_lines = self.invoice_id.invoice_line_ids

        line_ids = []
        for invoice_line in invoice_lines:
            line_vals = {"invoice_line_id": invoice_line.id}
            line_domain = [
                ("order_id", "=", self.purchase_order_id.id),
                ("product_id", "=", invoice_line.product_id.id),
            ]
            suggested = po_line.search(line_domain, limit=1)
            if suggested:
                line_vals["purchase_order_line_id"] = suggested.id

            line_ids.append((0, 0, line_vals))

        self.wizard_line_ids = [(5, 0, 0)] + line_ids
        self.wizard_line_ids._onchange_purchase_order_line_id()

    def action_confirm(self):
        self.ensure_one()

        for wizard_line in self.wizard_line_ids:
            invoice_line = wizard_line.invoice_line_id
            if wizard_line.purchase_order_line_id:
                vals = {
                    "purchase_line_id": wizard_line.purchase_order_line_id.id,
                    "account_id": wizard_line.account_id.id,
                    "price_unit": wizard_line.price_unit,
                    "quantity": wizard_line.quantity,
                }
                invoice_line.write(vals)

            invoice_line._onchange_purchase_line_id()

        return {"type": "ir.actions.act_window_close"}
