from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    stock_picking_waiting_payment_priority = fields.Integer(
        string="Picking priority when waiting down payments",
        config_parameter="stock.picking.waiting.payment.priority",
        default=0,
    )

    stock_picking_completed_payment_priority = fields.Integer(
        string="Picking priority after down payments",
        config_parameter="stock.picking.completed.payment.priority",
        default=1,
    )
