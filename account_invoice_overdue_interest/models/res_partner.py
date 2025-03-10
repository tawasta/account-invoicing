from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    overdue_interest = fields.Float(
        string="Overdue interest %",
        digits=(4, 2),
        help="Use this overdue interest for invoices. Leave at zero to use company default.",
    )

    @api.model
    def _commercial_fields(self):
        """Returns the list of fields that are managed by the commercial entity
        to which a partner belongs. These fields are meant to be hidden on
        partners that aren't `commercial entities` themselves, and will be
        delegated to the parent `commercial entity`. The list is meant to be
        extended by inheriting classes."""
        commercial_fields = super(ResPartner, self)._commercial_fields()
        return commercial_fields + ["overdue_interest"]
