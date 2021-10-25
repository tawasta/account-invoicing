##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2021- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import api, fields, models
from odoo.addons import decimal_precision as dp

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


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
    comment = fields.Text(string="Additional Information")

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
    @api.multi
    def confirm(self):

        invoice_model = self.env["account.invoice"]
        invoice_line_model = self.env["account.invoice.line"]
        partners = self.env["res.partner"].browse(self._context.get("active_ids"))
        invoice_type = "out_invoice"
        journal = invoice_model.with_context(
            {"invoice_type": invoice_type}
        )._default_journal()

        line_account_id = invoice_line_model.with_context(
            journal_id=journal.id, type=invoice_type
        )._default_account()

        invoice_values = {"journal_id": journal.id, "type": invoice_type}

        if self.payment_term_id:
            invoice_values["payment_term_id"] = self.payment_term_id.id

        if self.date_invoice:
            invoice_values["date_invoice"] = self.date_invoice

        if self.partner_bank_id:
            invoice_values["partner_bank_id"] = self.partner_bank_id.id

        if self.comment:
            invoice_values["comment"] = self.comment

        line_values = {
            "product_id": self.product_id.id,
            "name": self.line_name,
            "quantity": self.quantity,
            "price_unit": self.price_unit,
            "account_id": line_account_id,
            "uom_id": self.product_id.uom_id.id,
            "invoice_line_tax_ids": [(6, 0, self.product_id.taxes_id.ids)],
        }

        for partner in partners:
            invoice_values["partner_id"] = partner.id
            invoice_values["account_id"] = partner.property_account_receivable_id.id
            invoice_values[
                "fiscal_position_id"
            ] = partner.property_account_position_id.id
            invoice_values["message_follower_ids"] = False

            invoice = invoice_model.create(invoice_values)
            invoice.message_subscribe(
                [invoice.partner_id.id, self.env.user.partner_id.id]
            )
            line_values["invoice_id"] = invoice.id

            invoice_line_model.create(line_values)

    # 8. Business methods
