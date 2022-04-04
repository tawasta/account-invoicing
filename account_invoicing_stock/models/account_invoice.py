from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    stock_picking_ids = fields.Many2many(
        comodel_name="stock.picking", string="Stock picking", required=False
    )

    @api.multi
    def action_invoice_paid(self):
        paid_invoice = super(AccountInvoice, self).action_invoice_paid()
        if self.stock_picking_ids and self.state == 'paid':
            for pick in self.stock_picking_ids:
                all_invoices = pick.invoice_ids
                state_list = []
                for inv in all_invoices:
                    state_list.append(inv.state)

                result = all(element == state_list[0] for element in state_list)
                if result:
                    pick.sudo().write({'priority': '1'})
        return paid_invoice
