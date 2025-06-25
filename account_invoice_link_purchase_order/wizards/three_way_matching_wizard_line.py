import logging

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ThreeWayMatchingWizard(models.TransientModel):
    _name = "three.way.matching.wizard.line"
    _description = "Three way matching wizard line"

    wizard_id = fields.Many2one(comodel_name="three.way.matching.wizard")
    currency_id = fields.Many2one(related="invoice_line_id.currency_id")
    company_id = fields.Many2one(related="invoice_line_id.company_id")
    account_id = fields.Many2one(
        comodel_name="account.account",
        string="Account",
        domain="[('deprecated', '=', False), ('account_type', '!=', 'off_balance')]",
        check_company=True,
    )
    price_unit = fields.Float(
        string="Unit Price",
        required=True,
        digits="Product Price",
        help="Real unit price",
    )
    quantity = fields.Float(string="Invoiced", digits="Product Unit of Measure")

    invoice_line_id = fields.Many2one("account.move.line", required=True)
    purchase_order_line_id = fields.Many2one(
        "purchase.order.line", string="Purchase line", required=True
    )

    invoice_line_price_unit = fields.Float(
        related="invoice_line_id.price_unit",
        string="Invoice unit price",
    )
    purchase_order_line_price_unit = fields.Float(
        related="purchase_order_line_id.price_unit",
        string="PO unit price",
    )

    invoice_line_qty = fields.Float(
        related="invoice_line_id.quantity", string="Invoice Quantity"
    )
    purchase_line_qty = fields.Float(
        related="purchase_order_line_id.product_qty", string="Purchase Quantity"
    )

    purchase_line_qty_to_invoice = fields.Float(
        related="purchase_order_line_id.qty_to_invoice", string="To invoice"
    )

    purchase_line_subtotal = fields.Monetary(
        related="purchase_order_line_id.price_subtotal", string="Purchase subtotal"
    )
    invoice_line_subtotal = fields.Monetary(
        related="invoice_line_id.price_subtotal", string="Invoice subtotal"
    )

    @api.onchange("purchase_order_line_id")
    def _onchange_purchase_order_line_id(self):
        for record in self:
            invoice = record.wizard_id.invoice_id
            account_id = False
            fiscal_position = invoice.fiscal_position_id
            po_line = record.purchase_order_line_id
            record = record.with_company(invoice.company_id)

            accounts = po_line.product_id.product_tmpl_id.get_product_accounts(
                fiscal_pos=fiscal_position
            )
            if invoice.is_sale_document(include_receipts=True):
                account_id = accounts["income"] or record.account_id
            elif invoice.is_purchase_document(include_receipts=True):
                account_id = accounts["expense"] or record.account_id

            values = {
                "price_unit": record.purchase_order_line_id.price_unit,
                "quantity": record.purchase_order_line_id.qty_to_invoice,
                "account_id": account_id,
            }

            record.write(values)
