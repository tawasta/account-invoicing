from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    invoice_clause = fields.Many2one(
        "partner.clause", string="Invoice clause", copy=False, default=False
    )
