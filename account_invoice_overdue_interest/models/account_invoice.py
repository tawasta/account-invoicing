from odoo import api, fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.model
    def create(self, vals):
        """
        Override to add default overdue interest
        """
        if not vals.get('overdue_interest'):
            if vals.get('partner_id'):
                partner = self.env['res.partner'].browse([vals['partner_id']])
                # Overdue interest from partner or partner company
                vals['overdue_interest'] = \
                    partner.overdue_interest \
                    or partner.company_id.overdue_interest

        return super(AccountInvoice, self).create(vals)

    @api.onchange('partner_id')
    def onchange_partner_id_update_overdue_interest(self):
        """
        Change overdue interest on partner change
        """
        partner = self.partner_id

        if partner:
            # Overdue interest from partner or partner company
            self.overdue_interest = \
                partner.overdue_interest \
                or partner.company_id.overdue_interest

    overdue_interest = fields.Float(
        string='Overdue interest %',
        digits=(4, 2),
    )
