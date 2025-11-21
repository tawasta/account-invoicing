import inspect

from odoo import models

from odoo.addons.account_invoice_inter_company.models.account_move import (
    AccountMove as AccountMoveInter,
)


class AccountMove(models.Model):
    _inherit = "account.move"

    def _post(self, soft=True):
        res = super()._post(soft=soft)

        # Fetch the function in string format
        func = self.get_function_body(AccountMoveInter.action_post)

        # Remove super() and return to avoid errors
        func = func.replace("res = super().action_post()", "").replace("return res", "")

        # This is done because lambda does not notice supported_types variable
        func = func.replace(
            "x.move_type in supported_types",
            "x.move_type in {'out_invoice', 'in_invoice', 'out_refund', 'in_refund'}",
        )

        # Run the function
        exec(func)

        return res

    def get_function_body(self, func):
        """Get the body of a function"""

        def indentation(s):
            """Get the indentation"""
            return len(s) - len(s.lstrip())

        source = inspect.getsourcelines(func)[0]
        line_0 = source[0]
        ind_0 = indentation(line_0)
        body = []
        for line in source[1:]:
            ind = indentation(line)
            if ind > ind_0:
                body.append(line[(ind_0 + 4) :])
        return "".join(body)
