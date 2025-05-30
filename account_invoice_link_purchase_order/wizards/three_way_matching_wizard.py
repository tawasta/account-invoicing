import logging

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ThreeWayMatchingWizard(models.TransientModel):
    _name = "three.way.matching.wizard"
    _description = "Match purchase orders to invoice"

    invoice_id = fields.Many2one("account.move", string="Vendor Bill")
    purchase_order_id = fields.Many2one("purchase.order", string="Purchase Order")
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

    def action_confirm(self):
        self.ensure_one()

        for line in self.wizard_line_ids:
            if line.purchase_order_line_id:
                line.invoice_line_id.purchase_line_id = line.purchase_order_line_id

            line.invoice_line_id._onchange_purchase_line_id()

        return {"type": "ir.actions.act_window_close"}
