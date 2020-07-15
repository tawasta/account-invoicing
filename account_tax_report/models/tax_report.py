import base64
# import json
from collections import OrderedDict
from datetime import date, datetime

from odoo import api, fields, models

# from odoo .exceptions import Warning


class AccountTaxReport(models.Model):
    _name = "account_tax_report.tax.report"

    @api.model
    def _get_default_company(self):
        return self.env.user.company_id.id

    @api.model
    def _get_default_accounts(self):
        return self.env["account.account"].search([("tax_report", "=", True)]) or False

    @api.model
    def _get_default_period(self):
        period_start = date.today()
        period_end = date.today()
        return period_start and period_end

    """
    current_month = date.today().month
        if current_month > 1:
            current_month = -1

        first_day = date(
            date.today().year,
            date.today().month,
            1,
        ).strftime("%Y-%m-%d")
        res = self.env['account.period'].search([
            ('date_start', '=', first_day),
            ('company_id', '=', self.env.user.company_id.id)
        ])
        return res and res[0] or False
    """

    name = fields.Char(string="Name", default="/", compute="_get_name",)
    period_start = fields.Date(string="Period start", required=True,)
    period_end = fields.Date(string="Period end", required=True,)
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=_get_default_company,
        required=True,
    )
    period_id = fields.Many2one(
        comodel_name="account.period",
        string="Period",
        default=_get_default_period,
        # required=True,
    )
    report_file = fields.Binary(string="Download Report")
    filename = fields.Char(compute="_get_filename", string="Filename")
    line_ids = fields.One2many(
        "account_tax_report.tax.report.line", "report_id", string="Lines",
    )
    company_registry = fields.Char(
        string="Company Registry",
        related="company_id.company_registry",
        # required=True
    )
    account_ids = fields.Many2many(
        comodel_name="account.account",
        # 'account_account_rel',
        # 'acc_ids',
        # 'report_id',
        string="Accounts",
        default=_get_default_accounts,
        domain=[("tax_report", "=", True)],
        required=True,
    )
    partner_ids = fields.Many2many(
        comodel_name="res.partner",
        # 'partner_rel',
        # 'partner_ids',
        # 'report_id',
        compute="_get_partner_ids",
        string="Partners",
    )
    amount_total = fields.Float(string="Total amount", compute="_get_total_amounts",)
    amount_partners = fields.Integer(
        string="Total number of partners", compute="_get_total_amounts"
    )

    @api.model
    def _get_total_amounts(self):
        for report in self:
            amount_total = 0
            vat_codes = []
            for line in report.line_ids:
                amount_total += line.amount
                if line.vat_code not in vat_codes:
                    vat_codes.append(line.vat_code)

                    report.amount_total = amount_total
                    report.amount_partners = len(vat_codes)

    @api.model
    def _get_filename(self):
        if self.name != "/":
            self.filename = "ALV_yhteenveto_%s.csv" % self.name.replace(
                " ", "_"
            ).replace("/", "")
        else:
            self.filename = "ALV_yhteenveto.csv"

    @api.depends("line_ids")
    @api.model
    def _get_partner_ids(self):
        for record in self:
            for line in record.line_ids:
                if not line.partner_id.vat:
                    self.partner_ids = [(4, line.partner_id.id)]

    def _get_name(self):
        for record in self:
            name = "/"

            if record.period_start and record.period_end and record.company_id:
                company_name = record.company_id.name
                period_start = record.period_start
                period_end = record.period_end
                name = "{} {} - {}".format(company_name, period_start, period_end)

            record.name = name

    def _format_amounts(self, lines):
        vat_codes = []
        for _code, values in lines.items():
            for key, _value in values.items():

                if key == "103":
                    vatcode = values[key]
                    if vatcode in vat_codes:
                        print("duplicate vat code: %s" % vatcode)
                    vat_codes.append(vatcode)

                if key in ["210", "211", "212"]:
                    amount = values[key]
                    amount = "%.2f" % amount
                    values[key] = amount.replace(".", ",")

        return lines

    def _format_period(self, period):
        period = period[:2]
        if period[0] == "0":
            period = period[1:]
        return period

    def _format_country_code(self, code):
        """ Changes Greece code to EL that is used by ilmoitin.fi """
        if code == "GR":
            code = "EL"
        return code.replace(" ", "")

    def _format_vat_code(self, code):
        """ Removes country code from vat code"""
        if code:
            return code.replace(" ", "")[2:]
        else:
            return "NOVATCODE"

    def _get_timestamp(self):
        """ Returns current datetime in DDMMYYYYHHMMSS format"""
        # Returns the current datetime, taking into account
        # the current user's timezone
        now = fields.Datetime.context_timestamp(self, datetime.now())
        return now.strftime("%d%m%Y%H%M%S")

    def _get_tax_report_lines(self):
        res = OrderedDict()
        iterator = 1

        for line in self.line_ids:
            vatcode = self._format_vat_code(line.vat_code)
            if vatcode == "NOVATCODE":
                vatcode += str(iterator)

            if vatcode in res:
                res[vatcode]["210"] += line.amount
            else:
                vals = OrderedDict()
                vals["102"] = self._format_country_code(line.country_code)
                vals["103"] = vatcode
                vals["210"] = line.amount
                vals["211"] = 0.0
                vals["212"] = 0.0
                vals["009"] = iterator
                res[vatcode] = vals
                iterator += 1

        return res

    def _set_report_file(self):
        if self.line_ids:
            line_values = self._get_tax_report_lines()
            line_values = self._format_amounts(line_values)
            header = OrderedDict()
            header["000"] = "VSRALVYV"
            header["198"] = self._get_timestamp()
            header["010"] = self.company_registry
            header["052"] = self._format_period(self.period_id.code)
            header["053"] = self.period_id.fiscalyear_id.name
            header["001"] = self.amount_partners
            header_str = "\n".join(
                ["{}:{}".format(key, value) for key, value in header.items()]
            )
            line_str = ""
            for _code, line in line_values.items():
                line_str += "%s\n" % "\n".join(
                    ["{}:{}".format(key, value) for key, value in line.items()]
                )

            footer = OrderedDict()
            footer["048"] = "Futural ERP"
            footer["014"] = self.company_registry + "_V8"
            footer["999"] = "1"
            footer_str = "\n".join(
                ["{}:{}".format(key, value) for key, value in footer.items()]
            )

            report_str = header_str + "\n" + line_str + footer_str

            self.report_file = base64.encodestring(report_str)

    def _check_move_values(self, move):
        return (
            move.partner_id.country_id.eu_member
            and move.partner_id.country_id.code != "FI"
            and move.move_id.state == "posted"
            and (move.credit > 0 or move.debit > 0)
        )

    @api.multi
    def action_create_tax_report_lines(self):
        if not self.account_ids:
            print("No accounts selected.")
            # raise Warning("No accounts selected.")

        line_obj = self.env["account_tax_report.tax.report.line"]
        account_move_obj = self.env["account.move.line"]
        account_ids = [x.id for x in self.account_ids]

        for record in self:
            if record.line_ids:
                record.line_ids.unlink()

            move_domain = [
                # ('period_id', '=', record.period_id.id),
                ("date", ">=", record.period_start),
                ("date", "<=", record.period_end),
                ("account_id", "in", account_ids),
            ]

            move_ids = account_move_obj.search(move_domain)

            for move in move_ids:
                if self._check_move_values(move):
                    if move.credit > 0:
                        amount = move.credit
                    else:
                        amount = -move.debit

                vals = {
                    "partner_id": move.partner_id.id,
                    "country_code": move.partner_id.country_id.code,
                    "vat_code": move.partner_id.vat,
                    "amount": amount,
                    "product_id": move.product_id.id,
                    "product_type": move.product_id.type,
                    "report_id": self.id,
                    "move_line_id": move.id,
                }

                line_obj.create(vals)

            self._set_report_file()

        return True

    @api.multi
    def action_download_report(self):
        if self.partner_ids:
            partner_ids = [x.id for x in self.partner_ids]
            return {
                "name": "Missing VAT codes",
                "view_type": "form",
                "view_mode": "form",
                "type": "ir.actions.act_window",
                "target": "new",
                "res_model": "account_tax_report.info_window",
                "context": {
                    "default_report_id": self.id,
                    "default_filename": self.filename,
                    "default_partner_ids": partner_ids,
                },
            }
        else:
            return {
                "type": "ir.actions.act_url",
                "url": "/web/binary/download_document?model=account_tax_report\
                .tax.report&field=report_file&id=%s&filename=%s"
                % (self.id, self.filename),
                "target": "self",
            }

    @api.model
    def create(self, vals):
        name = self._get_name(vals)
        vals["name"] = name
        return super(AccountTaxReport, self).create(vals)

    @api.multi
    def write(self, vals):
        name = self._get_name(vals)
        vals["name"] = name
        return super(AccountTaxReport, self).write(vals)


class TaxReportLine(models.Model):
    _name = "account_tax_report.tax.report.line"

    report_id = fields.Many2one("account_tax_report.tax.report", string="Report Id")
    move_line_id = fields.Many2one("account.move.line")
    country_code = fields.Char(string="Country")
    vat_code = fields.Char(string="VAT")
    amount = fields.Float(string="Amount")
    product_type = fields.Char(string="Type")
    partner_id = fields.Many2one("res.partner", string="Partner")
    product_id = fields.Many2one("product.product", string="Product")


class TaxReportInfoWindow(models.TransientModel):
    _name = "account_tax_report.info_window"

    report_id = fields.Many2one("account_tax_report.tax.report")
    filename = fields.Char(string="Filename")
    partner_ids = fields.Many2many(
        "res.partner", "info_partner_rel", "partner_ids", "info_id", string="Partners"
    )

    @api.multi
    def action_recompute_lines(self):
        self.report_id.action_create_tax_report_lines()
        return {"type": "ir.actions.act_window.close"}

    @api.multi
    def action_create_report(self):
        return {
            "type": "ir.actions.act_url",
            "url": "/web/binary/download_document?model=account_tax_report\
            .tax.report&field=report_file&id=%s&filename=%s"
            % (self.report_id.id, self.filename),
            "target": "self",
        }
