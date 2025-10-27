from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"
    _order = "name_starts_upper desc, name asc, id desc"

    # Tähän tallennettu flagi: True, jos nimi alkaa isolla kirjaimella.
    name_starts_upper = fields.Boolean(
        string="Name Starts Upper",
        compute="_compute_name_starts_upper",
        store=True,
        index=True,
    )

    @api.depends("name")
    def _compute_name_starts_upper(self):
        for rec in self:
            n = (rec.name or "").strip()
            rec.name_starts_upper = bool(n and n[:1].isalpha() and n[:1].isupper())
