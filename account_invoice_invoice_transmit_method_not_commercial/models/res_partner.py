from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _commercial_fields(self):
        """
        Make the partner transmit methods non-commercial
        """
        res = super()._commercial_fields()
        if "customer_invoice_transmit_method_id" in res:
            res.remove("customer_invoice_transmit_method_id")
        if "supplier_invoice_transmit_method_id" in res:
            res.remove("supplier_invoice_transmit_method_id")
        return res
