from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    invoice_warn_msg = fields.Text(related="partner_id.invoice_warn_msg")
