from odoo import api
from odoo import models
from odoo import _


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.multi
    def name_get(self):
        """
        Overwrite the display name and create it without name
        """
        super(AccountInvoice, self).name_get()

        types = {
            'out_invoice': _('Invoice'),
            'in_invoice': _('Vendor Bill'),
            'out_refund': _('Credit Note'),
            'in_refund': _('Vendor Credit note'),
        }
        result = []
        for inv in self:
            result.append((inv.id, "%s" % inv.number or types[inv.type]))

        return result
