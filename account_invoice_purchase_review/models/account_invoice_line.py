from odoo import fields, models


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    partner_id = fields.Many2one(
        related='invoice_id.partner_id',
        store=True,
    )

    purchase_line_id = fields.Many2one(
        domain="[('partner_id', '=', partner_id)]",
    )
