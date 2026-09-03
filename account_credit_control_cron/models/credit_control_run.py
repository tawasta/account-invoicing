##############################################################################
#
#    Author: Futural Oy
#    Copyright 2026- Futural Oy (https://futural.fi)
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

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class CreditControlRun(models.Model):
    _inherit = "credit.control.run"

    @api.model
    def _cron_run_daily_credit_control(self):
        """Automate the manual credit control workflow for every company
        that has credit control policies configured:

            generate_credit_lines() -> set_to_ready_lines() -> run_channel_action()

        This is the same sequence a user runs by hand from Accounting >
        Credit Control > Runs. Email-channel lines get sent automatically;
        letter-channel lines are left in "to_be_sent" state for manual
        printing, exactly as a manual run would leave them.

        Skips a company for the day if a run already exists for today, so
        the cron stays safe to run more than once without creating
        duplicate runs/reminders.
        """
        today = fields.Date.context_today(self)

        for company in self.env["res.company"].sudo().search([]):
            policies = (
                self.env["credit.control.policy"]
                .sudo()
                .search(
                    [
                        "|",
                        ("company_id", "=", company.id),
                        ("company_id", "=", False),
                    ]
                )
            )
            if not policies:
                continue

            already_run = self.sudo().search_count(
                [("company_id", "=", company.id), ("date", "=", today)]
            )
            if already_run:
                continue

            try:
                with self.env.cr.savepoint():
                    run = (
                        self.sudo()
                        .with_company(company)
                        .create(
                            {
                                "date": today,
                                "company_id": company.id,
                                "policy_ids": [(6, 0, policies.ids)],
                            }
                        )
                    )
                    run.generate_credit_lines()
                    run.set_to_ready_lines()
                    run.run_channel_action()
            except Exception:
                _logger.exception(
                    "Automated credit control run failed for company %s (%s)",
                    company.name,
                    company.id,
                )
