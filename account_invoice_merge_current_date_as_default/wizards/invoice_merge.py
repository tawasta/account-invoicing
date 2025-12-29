from odoo import api, fields, models


class InvoiceMerge(models.TransientModel):
    _inherit = "invoice.merge"

    @api.model
    def default_get(self, fields_list):
        # Suggest current date in the invoice merge wizard

        res = super().default_get(fields_list)
        res["date_invoice"] = fields.Datetime.now()
        return res
