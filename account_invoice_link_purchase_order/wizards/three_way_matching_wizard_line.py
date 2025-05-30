import logging

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ThreeWayMatchingWizard(models.TransientModel):
    _name = "three.way.matching.wizard.line"
    _description = "Three way matching wizard line"

    wizard_id = fields.Many2one(comodel_name="three.way.matching.wizard")
    invoice_line_id = fields.Many2one("account.move.line")
    purchase_order_line_id = fields.Many2one(
        "purchase.order.line", string="Purchase line"
    )
    currency_id = fields.Many2one(related="invoice_line_id.currency_id")

    purchase_line_qty = fields.Float(
        related="purchase_order_line_id.product_qty", string="Purchase Quantity"
    )
    invoice_line_qty = fields.Float(
        related="invoice_line_id.quantity", string="Invoice Quantity"
    )

    purchase_line_subtotal = fields.Monetary(
        related="purchase_order_line_id.price_subtotal", string="Purchase subtotal"
    )
    invoice_line_subtotal = fields.Monetary(
        related="invoice_line_id.price_subtotal", string="Invoice subtotal"
    )
