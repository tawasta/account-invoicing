from odoo import fields, models


class AccountInvoiceReport(models.Model):

    _inherit = "account.invoice.report"

    product_template_id = fields.Many2one(
        "product.template", "Product Template", readonly=True
    )

    def _select(self):
        return (
            super(AccountInvoiceReport, self)._select()
            + ", line.product_tmpl_id as product_template_id"
        )
