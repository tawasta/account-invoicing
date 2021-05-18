from odoo import api
from odoo import fields
from odoo import models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    company_mismatch_journal_id = fields.Boolean(
        string="Company journal mismatch",
        compute="_compute_company_mismatch_journal_id",
    )
    company_mismatch_account_id = fields.Boolean(
        string="Company account mismatch",
        compute="_compute_company_mismatch_account_id",
    )
    company_mismatch_fiscal_position_id = fields.Boolean(
        string="Company fiscal position mismatch",
        compute="_compute_company_mismatch_fiscal_position_id",
    )
    company_mismatch_tax_ids = fields.Boolean(
        string="Company taxes mismatch", compute="_compute_company_mismatch_tax_ids",
    )
    company_mismatch_account_ids = fields.Boolean(
        string="Company accounts mismatch",
        compute="_compute_company_mismatch_account_ids",
    )

    @api.onchange("journal_id")
    def _compute_company_mismatch_journal_id(self):
        for record in self:
            if (
                record.journal_id
                and record.journal_id.company_id
                and record.journal_id.company_id != record.company_id
            ):
                record.company_mismatch_journal_id = True
            else:
                record.company_mismatch_journal_id = False

    @api.onchange("account_id")
    def _compute_company_mismatch_account_id(self):
        for record in self:
            if (
                record.account_id
                and record.account_id.company_id
                and record.account_id.company_id != record.company_id
            ):
                record.company_mismatch_account_id = True
            else:
                record.company_mismatch_account_id = False

    @api.onchange("fiscal_position_id")
    def _compute_company_mismatch_fiscal_position_id(self):
        for record in self:
            if (
                record.fiscal_position_id
                and record.fiscal_position_id.company_id
                and record.fiscal_position_id.company_id != record.company_id
            ):
                record.company_mismatch_fiscal_position_id = True
            else:
                record.company_mismatch_fiscal_position_id = False

    @api.depends("invoice_line_ids")
    def _compute_company_mismatch_tax_ids(self):
        for record in self:
            mismatch = False
            for line in record.invoice_line_ids:
                for tax in line.invoice_line_tax_ids:
                    if tax.company_id and tax.company_id != line.company_id:
                        mismatch = True

            record.company_mismatch_tax_ids = mismatch

    @api.depends("invoice_line_ids")
    def _compute_company_mismatch_account_ids(self):
        for record in self:
            mismatch = False
            for line in record.invoice_line_ids:
                if (
                    line.account_id.company_id
                    and line.account_id.company_id != line.company_id
                ):
                    mismatch = True

            record.company_mismatch_account_ids = mismatch
