from odoo import fields, models


class InvoiceMerge(models.TransientModel):

    _inherit = "invoice.merge"

    link_attachment = fields.Boolean(string="Link attachments", default=True)

    def merge_invoices(self):
        self.ensure_one()
        return super(
            InvoiceMerge, self.with_context(link_attachment=self.link_attachment)
        ).merge_invoices()
