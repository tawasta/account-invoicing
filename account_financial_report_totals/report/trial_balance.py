##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2022- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

# 1. Standard library imports:
import logging

# 3. Odoo imports (openerp):
from odoo import _, models

# 2. Known third party imports:


# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:

_logger = logging.getLogger(__name__)


class TrialBalanceReport(models.AbstractModel):
    # 1. Private attributes
    _inherit = "report.account_financial_report.trial_balance"

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    def _get_report_values(self, docids, data):
        res = super(TrialBalanceReport, self)._get_report_values(docids, data)
        show_partner_details = data["show_partner_details"]
        foreign_currency = data["foreign_currency"]
        if (
            not show_partner_details
            and "trial_balance" in res
            and res.get("trial_balance")
        ):
            total_trial_balance = {
                "id": False,
                "code": False,
                "name": _("Total"),
                "hide_account": False,
                "group_id": False,
                "currency_id": False,
                "currency_name": False,
                "centralized": False,
                "initial_balance": 0.0,
                "debit": 0.0,
                "credit": 0.0,
                "balance": 0.0,
                "ending_balance": 0.0,
                "ending_currency_balance": 0.0,
                "initial_currency_balance": 0.0,
                "type": "account_type",
                "complete_code": False,
                "level": 0,
            }
            for account in res.get("trial_balance"):
                total_trial_balance["initial_balance"] += account.get("initial_balance")
                total_trial_balance["debit"] += account.get("debit")
                total_trial_balance["credit"] += account.get("credit")
                total_trial_balance["balance"] += account.get("balance")
                total_trial_balance["ending_balance"] += account.get("ending_balance")
                if foreign_currency:
                    total_trial_balance["ending_currency_balance"] += account.get(
                        "ending_currency_balance"
                    )
                    total_trial_balance["initial_currency_balance"] += account.get(
                        "initial_currency_balance"
                    )

            _logger.debug("Totals appended to Trial Balance:\n%s" % total_trial_balance)
            res["trial_balance"].append(total_trial_balance)
        return res

    # 8. Business methods
