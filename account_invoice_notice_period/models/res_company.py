from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    notice_period = fields.Integer(
        string="Notice period (days)",
        help="Default notice period (days) for new customers and invoices",
        readonly=False,
    )
