from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    invoice_email = fields.Char(help="Email address used for invoicing purposes.")
