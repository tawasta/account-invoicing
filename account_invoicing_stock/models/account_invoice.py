from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    stock_picking_ids = fields.Many2many(
        comodel_name="stock.picking", string="Stock picking", required=False
    )

    @api.multi
    def action_invoice_paid(self):
        paid_invoice = super().action_invoice_paid()
        for record in self:
            if record.stock_picking_ids and record.state == "paid":
                for pick in record.stock_picking_ids:
                    all_invoices = pick.invoice_ids
                    state_list = []
                    for inv in all_invoices:
                        state_list.append(inv.state)

                    result = all(element == state_list[0] for element in state_list)
                    if result:
                        pick.sudo().write({"priority": "1"})
        return paid_invoice
