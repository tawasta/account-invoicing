from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    stock_picking_waiting_payment_priority = fields.Char(
        string="Picking priority when waiting down payments",
        config_parameter="stock.picking.waiting.payment.priority",
        default="0",
    )

    stock_picking_completed_payment_priority = fields.Char(
        string="Picking priority after down payments",
        config_parameter="stock.picking.completed.payment.priority",
        default="1",
    )

    @api.constrains(
        "stock_picking_waiting_payment_priority",
        "stock_picking_completed_payment_priority",
    )
    def _check_stock_picking_priority(self):
        for record in self:
            # TODO: check if the priority value actually exists
            try:
                int(record.stock_picking_waiting_payment_priority)
                int(record.stock_picking_completed_payment_priority)
            except ValueError as e:
                raise ValidationError(
                    _("Please use numeric values for picking priority")
                ) from e
