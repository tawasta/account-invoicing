from odoo import api, fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    def get_invoices_customs_decision(self, moves):
        moves_decision = self.env["account.move"]

        for move in moves:
            if move.move_type != "out_invoice":
                continue

            att = self.env["ir.attachment"]
            attachments = att.search(
                [("res_id", "=", move.id), ("res_model", "=", "account.move")]
            )
            if not attachments or len(attachments) <= 1:
                continue

            out_eu = (
                move.fiscal_position_id
                and move.fiscal_position_id.fiscal_type == "non_eu"
                or False
            )
            if out_eu:
                moves_decision += move
        yield moves_decision

    @api.depends("fiscal_position_id")
    def _compute_many_attachments(self):
        # It is faster to use this python generator
        moves_decision = self.get_invoices_customs_decision(self)

        moves_no_decision = self

        for move in moves_decision:
            move.many_attachments = True
            move.many_attachments_false = False
            moves_no_decision -= move
        for move in moves_no_decision:
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
