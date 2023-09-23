from odoo import api, models


class AccountMoveLine(models.Model):

    _inherit = "account.move.line"

    @api.onchange("analytic_account_id")
    def onchange_analytic_account_id_update_analytic_tags(self):
        for rec in self:
            if rec.analytic_account_id and rec.analytic_account_id.tag_ids:
                rec.analytic_tag_ids += (
                    rec.analytic_account_id.tag_ids - rec.analytic_tag_ids
                )
