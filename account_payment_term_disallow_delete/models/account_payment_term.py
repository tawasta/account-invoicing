from odoo import _, models
from odoo.exceptions import ValidationError


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    def unlink(self):
        for record in self:
            # Check partner payment terms
            partner_payment_terms = (
                self.env["ir.property"]
                .sudo()
                .search(
                    [
                        ("name", "=", "property_payment_term_id"),
                        (
                            "value_reference",
                            "=",
                            "account.payment.term,{}".format(record.id),
                        ),
                    ]
                )
            )

            if partner_payment_terms:
                raise ValidationError(
                    _(
                        "Payment term is in use for partners. "
                        "Please archive it instead of deleting."
                    )
                )

            # Check for sale payment terms
            sale_payment_terms = self.env["sale.order"].search(
                [("payment_term_id", "=", record.id)]
            )

            if sale_payment_terms:
                raise ValidationError(
                    _(
                        "Payment term is in use for Sale Orders. "
                        "Please archive it instead of deleting."
                    )
                )

            # Check for purchase payment terms
            purchase_payment_terms = self.env["purchase.order"].search(
                [("payment_term_id", "=", record.id)]
            )

            if purchase_payment_terms:
                raise ValidationError(
                    _(
                        "Payment term is in use for Purchase Orders. "
                        "Please archive it instead of deleting."
                    )
                )

            # Check for invoice payment terms
            invoice_payment_terms = self.env["account.move"].search(
                [("invoice_payment_term_id", "=", record.id)]
            )

            if invoice_payment_terms:
                raise ValidationError(
                    _(
                        "Payment term is in use for invoices. "
                        "Please archive it instead of deleting."
                    )
                )

        return super().unlink()
