
from odoo import api, models, _


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _prepare_invoice(self):
        """Assign phone and email values to Invoice's comment-field"""
        vals = super(SaleOrder, self)._prepare_invoice()
        email = self.user_id.partner_id.email
        note = vals['comment']

        # Conditions to add newlines
        email_line = '\n' if note else ''

        if email:
            vals['comment'] += '{}{}{}'.format(email_line, _("Handler: "),
                                               email)

        vals['salesperson_email'] = self.user_id.partner_id.email
        return vals
