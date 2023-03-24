from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

from odoo.addons import decimal_precision as dp


class AccountInvoiceMassCreate(models.TransientModel):
    # 1. Private attributes
    _name = "account.invoice.mass.create"

    # 2. Fields declaration
    product_id = fields.Many2one(comodel_name="product.product", required=True)
    price_unit = fields.Float(
        string="Unit Price", required=True, digits=dp.get_precision("Product Price")
    )
    quantity = fields.Float(
        string="Quantity",
        digits=dp.get_precision("Product Unit of Measure"),
        required=True,
        default=1,
    )
    line_name = fields.Char(string="Description", required=True)

    payment_term_id = fields.Many2one(
        comodel_name="account.payment.term", string="Payment Terms"
    )
    date_invoice = fields.Date(string="Invoice Date")
    partner_bank_id = fields.Many2one(
        comodel_name="res.partner.bank",
        string="Bank Account",
        domain=lambda self: [
            ("partner_id", "=", self.env.user.company_id.partner_id.id)
        ],
    )
    narration = fields.Text(string="Additional Information")

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.onchange("product_id")
    def onchange_product_id(self):
        for record in self:
            product = record.product_id
            record.price_unit = product.lst_price
            record.line_name = product.description_sale or product.name

    # 6. CRUD methods

    # 7. Action methods
    def confirm(self):
        invoice_model = self.env["account.move"]
        invoice_line_model = self.env["account.move.line"]
        partners = self.env["res.partner"].browse(self._context.get("active_ids"))

        invoice_values = {
            "move_type": "out_invoice",
        }

        if self.payment_term_id:
            invoice_values["invoice_payment_term_id"] = self.payment_term_id.id

        if self.date_invoice:
            invoice_values["invoice_date"] = self.date_invoice

        if self.partner_bank_id:
            invoice_values["partner_bank_id"] = self.partner_bank_id.id

        if self.narration:
            invoice_values["narration"] = self.narration

        account = self.product_id.product_tmpl_id._get_product_accounts()

        line_values = {
            "product_id": self.product_id.id,
            "name": self.line_name,
            "quantity": self.quantity,
            "price_unit": self.price_unit,
            "product_uom_id": self.product_id.uom_id.id,
            "account_id": account["income"].id,
            "tax_ids": [(6, 0, self.product_id.taxes_id.ids)],
        }

        invoices = []
        for partner in partners:
            if (
                partner.invoice_warn == "block"
                or partner.commercial_partner_id.invoice_warn == "block"
            ):
                warn = (
                    partner.invoice_warn_msg
                    or partner.commercial_partner_id.invoice_warn_msg
                )
                raise ValidationError(
                    _("Can't create invoice for {}: {}".format(partner.name, warn))
                )

            invoice_values.update(
                {
                    "partner_id": partner.id,
                    "fiscal_position_id": partner.property_account_position_id.id,
                    "message_follower_ids": False,
                }
            )
            invoice_values["partner_id"] = partner.id

            invoice = invoice_model.create(invoice_values)
            invoices.append(invoice.id)
            invoice.message_subscribe(
                [invoice.partner_id.id, self.env.user.partner_id.id]
            )
            line_values["move_id"] = invoice.id

            invoice_line_model.with_context(check_move_validity=False).create(
                line_values
            )

        return self.action_view_invoices(invoices)

    def action_view_invoices(self, invoices):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "account.action_move_out_invoice_type"
        )
        action["domain"] = [("id", "in", invoices)]
        action["context"] = {"default_move_type": "out_invoice"}

        return action

    # 8. Business methods
