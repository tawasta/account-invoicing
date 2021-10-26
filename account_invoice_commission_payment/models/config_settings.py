from odoo import fields
from odoo import models


class ConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    commission_communication = fields.Char(related='company_id.commission_communication', readonly=False)
