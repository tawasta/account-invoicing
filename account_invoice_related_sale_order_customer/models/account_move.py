from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    sale_partner_id = fields.Many2one("res.partner", related="sale_id.partner_id")
