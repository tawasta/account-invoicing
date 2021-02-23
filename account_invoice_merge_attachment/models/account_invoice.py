from odoo import api, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.multi
    def do_merge(self, keep_references=True, date_invoice=False):
        invoices_info = super(AccountInvoice, self).do_merge(
            keep_references=keep_references, date_invoice=date_invoice)

        if self.env.context.get('link_attachment'):
            AttachmentObj = self.env['ir.attachment']
            for new_invoice_id in invoices_info:
                old_invoice_ids = invoices_info[new_invoice_id]
                attachs = AttachmentObj.search([
                    ('res_model', '=', self._name),
                    ('res_id', 'in', old_invoice_ids)
                ])
                for attach in attachs:
                    attach.copy(default={
                        'res_id': new_invoice_id,
                        'name': attach.name
                    })

        return invoices_info
