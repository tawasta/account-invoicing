from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    partner_customer_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer",
        readonly=True,
        states={'draft': [('readonly', False)]},
        track_visibility='always'
    )
