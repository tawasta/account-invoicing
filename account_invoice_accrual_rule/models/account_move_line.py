from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    accrual_rule_id = fields.Many2one(
        comodel_name="account.accrual.rule",
        string="Accrual rule",
    )

    @api.onchange("product_id")
    def onchange_product_id_set_accrual_rule(self):
        for record in self:
            if record.product_id:
                record.accrual_rule_id = (
                    record.product_id.product_tmpl_id.accrual_rule_id
                )
            else:
                record.accrual_rule_id = False

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            product = self.env["product.product"].browse(vals.get("product_id"))
            accrual_rule = product.product_tmpl_id.accrual_rule_id
            if not vals.get("accrual_rule_id") and product and accrual_rule:
                vals["accrual_rule_id"] = accrual_rule.id

        res = super().create(vals_list)

        return res
