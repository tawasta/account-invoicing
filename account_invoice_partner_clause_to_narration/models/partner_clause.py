from odoo import fields, models


class PartnerClause(models.Model):

    _name = "partner.clause"

    name = fields.Char(string="Name")
    clause = fields.Text(
        string="Invoice clause", help="This text is added to invoice's narration field."
    )
