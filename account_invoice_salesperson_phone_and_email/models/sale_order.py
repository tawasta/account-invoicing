
from odoo import api, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _prepare_invoice(self):
        """Assign phone and email values to Invoice's comment-field"""
        vals = super(SaleOrder, self)._prepare_invoice()

        phone, email = (self.user_id.partner_id.phone,
                        self.user_id.partner_id.email)

        note = vals['comment']

        # Conditions to add newlines
        email_line = '\n' if note or phone else ''
        phone_line = '\n' if note else ''

        vals['comment'] = "%s%s%s" % (
            '%s' % note if note else '',
            '%s%s' % (phone_line, phone) if phone else '',
            '%s%s' % (email_line, email) if email else ''
        )

        return vals
