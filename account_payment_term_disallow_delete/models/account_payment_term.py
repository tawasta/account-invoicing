from odoo import models
from odoo.exceptions import ValidationError


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    def unlink(self):
        for record in self:
            # Check partner sale payment terms
            partner_payment_terms = self.env["res.partner"].search(
                [("property_payment_term_id", "=", record.id)]
            )

            if partner_payment_terms:
                raise ValidationError(
                    self.env_(
                        "Payment term is in use for partners. "
                        "Please archive it instead of deleting."
                    )
                )

            # Check partner purchase payment terms
            partner_payment_terms = self.env["res.partner"].search(
                [("property_supplier_payment_term_id", "=", record.id)]
            )

            if partner_payment_terms:
                raise ValidationError(
                    self.env_(
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
                    self.env_(
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
                    self.env_(
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
                    self.env_(
                        "Payment term is in use for invoices. "
                        "Please archive it instead of deleting."
                    )
                )

        return super().unlink()
