from odoo import api, models


class PaymentProvider(models.Model):
    _inherit = "payment.provider"

    @api.model
    def _get_compatible_providers(
        self, company_id, partner_id, amount, currency_id=None, **kwargs
    ):
        """Add handling for the new all_strict mode"""
        providers = super()._get_compatible_providers(
            company_id, partner_id, amount, currency_id=currency_id, **kwargs
        )
        order_id = kwargs.get("order_id") or kwargs.get("sale_order_id")

        mode = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("product_acquirer_settings.product_acquirer_restriction_mode")
        )
        if mode != "all_strict" or not order_id:
            return providers

        order = self.env["sale.order"].sudo().browse(order_id).exists()

        # Products without allowed providers set will accept any provider, so leave
        # those products out from the check
        restricted_products = order.order_line.product_id.filtered(
            "allowed_payment_provider_ids"
        )

        # Keep only the providers that every restricted product allows
        return providers.filtered(
            lambda provider: all(
                provider in product.allowed_payment_provider_ids
                for product in restricted_products
            )
        )
