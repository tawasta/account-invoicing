from odoo import models, fields, _


class AccountInvoiceCommissionPaymentWizard(models.TransientModel):
    _inherit = "account.invoice.commission.payment.wizard"

    commission_partner = fields.Selection(
        selection_add=[("product_variant_company", "Product variant owner")],
        ondelete={"product_variant_company": "set default"},
    )

    def get_commission_partner(self, invoice_line):
        partner_id = super().get_commission_partner(invoice_line)

        if self.commission_partner == "product_variant_company":
            partner_id = invoice_line.product_id.variant_company_id.partner_id

        return partner_id
