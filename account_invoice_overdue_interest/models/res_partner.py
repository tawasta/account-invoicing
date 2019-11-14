from odoo import fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    def _get_overdue_interest(self):
        if self.company_id:
            return self.company_id.overdue_interest
        else:
            return self.env.user.company_id.overdue_interest

    overdue_interest = fields.Float(
        string='Overdue interest %',
        digits=(4, 2),
        default=_get_overdue_interest,
        help='Default overdue interest % for customer invoices'
    )
