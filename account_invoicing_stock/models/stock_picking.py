from odoo import api
from odoo import fields
from odoo import models
from odoo import _
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    # 2. Fields declaration
    invoice_ids = fields.One2many(
        string="Invoices",
        comodel_name="account.invoice",
        inverse_name="stock_picking_ids",
    )

    invoice_count = fields.Integer(
        compute="_compute_invoices",
        string="# of invoices",
        readonly=True,
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    def _compute_invoices(self):
        # Calculate the number of support activies so that the count can be
        # shown in the action button
        for invoice in self:
            invoice.invoice_count = len(invoice.invoice_ids)

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    @api.multi
    def action_view_invoice(self):
        invoice = self.mapped("invoice_ids")
        action = self.env.ref("account.action_invoice_tree1").read()[
            0
        ]

        if len(invoice) == 0:
            form_view_name = "account.invoice_form"
            action["views"] = [(self.env.ref(form_view_name).id, "form")]
        else:
            action["domain"] = [("id", "in", invoice.ids)]

        return action

    @api.multi
    def button_validate(self):
        invoices = self.env["account.invoice"].sudo().search([
            ('stock_picking_ids', 'in', self.id)
        ])
        status_list = []
        for inv in invoices:
            if inv.state == 'paid':
                status_list.append(inv.state)

        if len(invoices) == len(status_list):
            return super(StockPicking, self).button_validate()
        else:
            raise ValidationError(_('You cannot confirm the transfer because some of the invoices are still pending!'))
        

    # 8. Business methods
