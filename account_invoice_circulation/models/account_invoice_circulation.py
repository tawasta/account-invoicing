from odoo import api, fields, models


class AccountInvoiceCirculation(models.Model):

    _name = "account.invoice.circulation"
    _description = "Invoice circulation rule"

    name = fields.Char(string="Invoice circulation", required=True)

    user_id = fields.Many2one(
        comodel_name="res.users", string="Validator", required=True
    )

    circulation_line_ids = fields.One2many(
        comodel_name="account.invoice.circulation.line",
        inverse_name="circulation_id",
        string="Approvers",
    )

    active = fields.Boolean(default=True)

    @api.model
    def create(self, values):
        res = super().create(values)

        res._update_line_sequence()

        return res

    def write(self, values):
        res = super().write(values)

        self._update_line_sequence()

        return res

    def _update_line_sequence(self):
        for record in self:
            # Check if the sequences aren't set
            sequences = record.circulation_line_ids.mapped("sequence")

            if len(sequences) == len(set(sequences)):
                # No duplicates. Don't do anything
                continue

            # Sequences are ambiguous or not set. Recalculate them
            for index, line in enumerate(record.circulation_line_ids):
                line.sequence = index
