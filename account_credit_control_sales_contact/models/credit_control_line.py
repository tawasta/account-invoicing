from odoo import _, models, api, fields
from odoo.exceptions import UserError


class CreditControlLine(models.Model):

    _inherit = "credit.control.line"

    sales_agent = fields.Many2one(
        string="Sales contact",
        comodel_name="sales.agent",
        compute="_compute_sales_agent_id",
        store=True,
    )

    @api.depends("partner_id.sales_agent")
    def _compute_sales_agent_id(self):
        for line in self:
            line.sales_agent = line.partner_id.sales_agent
