from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    ref_invoice_id = fields.Many2one(
        string="Invoice origin",
        comodel_name="account.move",
        compute="_compute_ref_invoice_id",
        store=True,
        copy=False,
    )

    @api.depends("ref")
    def _compute_ref_invoice_id(self):
        for record in self:
            ref_invoice_id = False
            if record.ref:
                res = (
                    self.env["account.move"].sudo().search([("name", "=", record.ref)])
                )
                if res and len(res) == 1:
                    ref_invoice_id = res.id

            record.ref_invoice_id = ref_invoice_id
