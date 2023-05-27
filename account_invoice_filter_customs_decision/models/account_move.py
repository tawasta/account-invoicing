from odoo import api, fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    @api.depends("fiscal_position_id")
    def _compute_many_attachments(self):
        att = self.env["ir.attachment"]
        for move in self:
            attachments = att.search(
                [("res_id", "=", move.id), ("res_model", "=", "account.move")]
            )

            out_eu = (
                move.fiscal_position_id
                and move.fiscal_position_id.fiscal_type == "non_eu"
                or False
            )

            if out_eu and attachments and len(attachments.ids) > 1:
                move.many_attachments = True
                move.many_attachments_false = False
            else:
                move.many_attachments = False
                move.many_attachments_false = True

    # Timo: I could not make this work with one field. Feel free to remove
    # many_attachments_false field, if you can make filtering work for False
    # values of many_attachments-field.
    many_attachments = fields.Boolean(
        compute="_compute_many_attachments", search="_search_many_attachments"
    )
    many_attachments_false = fields.Boolean(
        compute="_compute_many_attachments", search="_search_many_attachments_false"
    )

    def _search_many_attachments(self, operator, value):
        recs = self.search([]).filtered(lambda x: x.many_attachments is True)
        if recs:
            return [("id", "in", [x.id for x in recs])]

    def _search_many_attachments_false(self, operator, value):
        recs = self.search([]).filtered(lambda x: x.many_attachments_false is True)
        if recs:
            return [("id", "in", [x.id for x in recs])]
