from odoo import api, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.multi
    def action_invoice_open(self):

        for record in self:
            if record.origin:
                origin = "Origin: {}".format(record.origin)

                if record.description:
                    record.description += "\n{}".format(origin)
                else:
                    record.description = origin

        return super(AccountInvoice, self).action_invoice_open()
