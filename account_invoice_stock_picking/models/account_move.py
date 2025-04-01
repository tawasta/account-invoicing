from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    stock_picking_ids = fields.Many2many(
        comodel_name="stock.picking",
        string="Stock pickings",
        required=False,
        copy=False,
        compute="_compute_stock_picking_ids",
    )

    def _compute_stock_picking_ids(self):
        for record in self:
            # Get all related pickings
            stock_pickings = record.invoice_line_ids.mapped(
                "sale_line_ids.order_id.picking_ids"
            )
            record.stock_picking_ids = stock_pickings

    def action_show_stock_pickings(self):
        self.ensure_one()

        form_view_name = "stock.view_picking_form"
        xmlid = "stock.action_picking_tree_all"
        action = self.env["ir.actions.act_window"]._for_xml_id(xmlid)

        if len(self.stock_picking_ids) > 1:
            action["domain"] = [("id", "in", self.stock_picking_ids.ids)]
        else:
            form_view = self.env.ref(form_view_name)
            action["views"] = [(form_view.id, "form")]
            action["res_id"] = self.stock_picking_ids.id

        return action
