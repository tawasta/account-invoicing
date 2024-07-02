from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    commission_communication = fields.Char(
        string="Default commission communication", translate=True
    )
