from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    hide_invoice_name = fields.Boolean(string="Hide invoice name")
