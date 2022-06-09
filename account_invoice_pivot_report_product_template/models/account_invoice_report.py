from odoo import fields, models


class AccountInvoiceReport(models.Model):

    _inherit = "account.invoice.report"

    product_template_id = fields.Many2one(
        "product.template", "Product Template", readonly=True
    )

    def _select(self):
        return super(AccountInvoiceReport, self)._select() + ", sub.product_template_id"

    def _sub_select(self):
        return (
            super(AccountInvoiceReport, self)._sub_select()
            + ", pr.product_tmpl_id AS product_template_id"
        )

    def _from(self):
        return (
            super(AccountInvoiceReport, self)._from()
            + """ LEFT JOIN product_template prt ON
            prt.id = pt.id"""
        )

    def _group_by(self):
        return super(AccountInvoiceReport, self)._group_by() + ", pr.product_tmpl_id"
