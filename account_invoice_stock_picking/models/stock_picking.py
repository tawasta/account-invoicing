from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    invoice_ids = fields.Many2many(
        comodel_name="account.move",
        related="sale_id.invoice_ids",
    )

    invoice_count = fields.Integer(
        related="sale_id.invoice_count",
    )

    def action_view_invoice(self):
        self.ensure_one()
        form_view_name = "account.view_move_form"
        xmlid = "account.action_move_out_invoice_type"
        action = self.env["ir.actions.act_window"]._for_xml_id(xmlid)
        if len(self.invoice_ids) > 1:
            action["domain"] = [("id", "in", self.invoice_ids.ids)]
        else:
            form_view = self.env.ref(form_view_name)
            action["views"] = [(form_view.id, "form")]
            action["res_id"] = self.invoice_ids.id

        return action
