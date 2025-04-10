from odoo import models
import logging

_logger = logging.getLogger(__name__)


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def account_move_line_type_fixer(
        self, from_year=False, to_year=False, account_id=False
    ):
        if not account_id:
            _logger.info("Account has not been set to run account_move_line_type_fixer")
            return

        if not from_year or not to_year:
            _logger.info("Years have not been set to run account_move_line_type_fixer")
            return

        years = []

        dif = 0

        while (from_year + dif - 1) < to_year:
            years.append(
                [
                    ("create_date", ">", "{}-01-01 00:00:00".format(to_year - dif)),
                    ("create_date", "<", "{}-06-01 00:00:00".format(to_year - dif)),
                ]
            )

            years.append(
                [
                    ("create_date", ">", "{}-06-01 00:00:00".format(to_year - dif)),
                    ("create_date", "<", "{}-01-01 00:00:00".format(to_year + 1 - dif)),
                ]
            )

            dif += 1

        for year in years:
            job_desc = "Fixing account move line type in year {}".format(year)
            self.with_delay(description=job_desc)._account_move_line_type_fix(
                year_domain=year, account=account_id
            )
            _logger.info("Done fixing account move line for year {}".format(year))

    def _account_move_line_type_fix(self, year_domain, account):
        search_domain = [
            ("account_id", "=", account),
            ("display_type", "=", "product"),
            ("payment_id", "=", False),
            ("tax_line_id", "=", False),
        ]

        search_domain = search_domain + year_domain

        lines = self.env["account.move.line"].search(search_domain)

        i = 0
        count = len(lines)
        _logger.info(
            "{} account move lines with potentially incorrect display type found".format(
                count
            )
        )

        for line in lines:
            i += 1
            _logger.info(f"Line {line.id} ({i}/{count})")
            account_type = line.account_id.account_type

            if account_type != "asset_receivable":
                # Only fix "asset_receivable"-lines
                continue

            account_set = line.account_id
            tax_set = line.tax_line_id

            # Get the display type the same way as _compute_display_type(), but without referring to cache
            display_type = (
                (
                    "tax"
                    if tax_set and line.tax_line_id
                    else "payment_term"
                    if account_set
                    and line.account_id.account_type
                    in ["asset_receivable", "liability_payable"]
                    else "product"
                )
                if line.move_id.is_invoice()
                else "product"
            )

            if line.display_type != display_type:
                # If the display type doesn't match, overwrite it
                _logger.info(
                    f"Changing account move line {line.id} type from '{line.display_type}' to '{display_type}'"
                )
                try:
                    line.write({"display_type": display_type})
                except Exception as e:
                    _logger.error(e)
