from odoo import fields
from odoo import models
from odoo.addons import decimal_precision as dp


class ResCompany(models.Model):

    _inherit = "res.company"

    commission_communication = fields.Char(string='Default commission communication', translate=True)
