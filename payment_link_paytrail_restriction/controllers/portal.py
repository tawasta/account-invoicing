from odoo import http

from odoo.addons.payment.controllers.portal import PaymentPortal


class PaytrailPaymentPortal(PaymentPortal):
    @http.route()
    def payment_pay(
        self,
        reference=None,
        amount=None,
        currency_id=None,
        partner_id=None,
        company_id=None,
        access_token=None,
        **kwargs
    ):
        response = super(PaytrailPaymentPortal, self).payment_pay(
            reference=reference,
            amount=amount,
            currency_id=currency_id,
            partner_id=partner_id,
            company_id=company_id,
            access_token=access_token,
            **kwargs
        )

        payment_methods_sudo = response.qcontext.get(
            "payment_methods_sudo", []
        ).filtered(lambda method: method.code == "paytrail")

        response.qcontext.update(
            {
                "payment_methods_sudo": payment_methods_sudo,
            }
        )

        return response
