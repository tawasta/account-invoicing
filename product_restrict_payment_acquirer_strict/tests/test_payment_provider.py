from odoo.tests import TransactionCase, tagged

PARAM = "product_acquirer_settings.product_acquirer_restriction_mode"


@tagged("post_install", "-at_install")
class TestPaymentProviderStrict(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        Provider = cls.env["payment.provider"]
        cls.provider_a = Provider.create(
            {"name": "Strict A", "code": "none", "state": "test"}
        )
        cls.provider_b = Provider.create(
            {"name": "Strict B", "code": "none", "state": "test"}
        )
        cls.test_providers = cls.provider_a | cls.provider_b

        cls.partner = cls.env["res.partner"].create({"name": "Strict customer"})

        Product = cls.env["product.product"]
        cls.product_a = Product.create(
            {
                "name": "Only A",
                "allowed_payment_provider_ids": [(4, cls.provider_a.id)],
            }
        )
        cls.product_ab = Product.create(
            {
                "name": "A or B",
                "allowed_payment_provider_ids": [(6, 0, cls.test_providers.ids)],
            }
        )
        cls.product_b = Product.create(
            {
                "name": "Only B",
                "allowed_payment_provider_ids": [(4, cls.provider_b.id)],
            }
        )
        cls.product_free = Product.create({"name": "No restriction"})

        cls.env["ir.config_parameter"].set_param(PARAM, "all_strict")

    def _get_providers(self, products):
        order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "order_line": [
                    (0, 0, {"product_id": product.id, "product_uom_qty": 1.0})
                    for product in products
                ],
            }
        )
        return self.env["payment.provider"]._get_compatible_providers(
            self.env.company.id,
            self.partner.id,
            100,
            sale_order_id=order.id,
        )

    def test_common_provider(self):
        """Only the provider allowed by every product is offered"""
        providers = self._get_providers(self.product_a | self.product_ab)
        self.assertEqual(providers, self.provider_a)

    def test_no_common_provider(self):
        """Products without a common provider leave no payment option"""
        providers = self._get_providers(self.product_a | self.product_b)
        self.assertFalse(providers)

    def test_unrestricted_line_is_ignored(self):
        """A line without allowed providers does not lift the restriction"""
        providers = self._get_providers(self.product_a | self.product_free)
        self.assertEqual(providers, self.provider_a)

        # Line order must not matter
        providers = self._get_providers(self.product_free | self.product_a)
        self.assertEqual(providers, self.provider_a)

    def test_no_restricted_product(self):
        """Without any restricted product the standard providers are offered"""
        providers = self._get_providers(self.product_free)
        self.assertEqual(providers & self.test_providers, self.test_providers)

    def test_other_modes_unchanged(self):
        """The parent module's 'all' mode still falls back when nothing matches"""
        self.env["ir.config_parameter"].set_param(PARAM, "all")
        providers = self._get_providers(self.product_a | self.product_b)
        self.assertEqual(providers & self.test_providers, self.test_providers)
