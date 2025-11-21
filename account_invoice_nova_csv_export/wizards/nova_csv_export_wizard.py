import base64
import csv
import io
import logging
from datetime import timedelta

from odoo import _, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class NovaCSVExportWizard(models.TransientModel):
    _name = "nova.csv.export.wizard"
    _description = "Nova CSV Export Wizard"

    file_data = fields.Binary("CSV File", readonly=True)
    file_name = fields.Char("Filename", readonly=True)

    def export_nova_csv(self):
        # Read the selected invoices' contents and create+return a single CSV
        # out of them

        active_ids = self.env.context.get("active_ids", [])
        invoices = self.env["account.move"].browse(active_ids)

        self._pre_validate_data(invoices)

        output = io.StringIO()
        writer = csv.writer(
            output, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

        # Write the fixed header rows
        writer.writerows(self._prepare_static_headers())

        # Write each invoice header row, followed by that invoice's invoice line rows
        for invoice in invoices:
            writer.writerow(self._prepare_invoice_row(invoice))

            # Mimic the sequence of 11, 21, 31... of the example file.
            running_number = 11
            for line in invoice.invoice_line_ids:
                writer.writerow(
                    self._prepare_invoice_line_row(invoice, line, running_number)
                )
                running_number += 10

            # Log the timestamp to the invoice
            invoice.last_nova_csv_export = fields.Datetime.now()

        csv_charset = self._get_csv_charset()

        csv_data = base64.b64encode(output.getvalue().encode(csv_charset))
        output.close()

        filename = (
            f"nova_invoices_{fields.Datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
        )

        self.write({"file_data": csv_data, "file_name": filename})

        # Autodownload the created file
        return {
            "type": "ir.actions.act_url",
            "url": f"/web/content/?model={self._name}&id={self.id}&field=file_data&download=true&filename={filename}",  # noqa: E501
            "target": "self",
        }

    def _get_csv_charset(self):
        # TODO verify what the receiving end expects. It's not UTF8.
        # Potentially cp1252 or iso-8859-1?
        return "cp1252"

    def _pre_validate_data(self, invoices):
        # Run some preliminary checks before exporting
        # TODO: add some more

        errors = []

        # Validate all are customer invoices
        if any(inv.move_type != "out_invoice" for inv in invoices):
            errors.append(_("Only customer invoices can be exported."))

        if len(errors):
            errors_heading_string = _(
                "Please fix the following issues before exporting: <br/>"
            )

            errors_string = errors.split(", ")

            raise ValidationError(errors_heading_string + errors_string)

    def _prepare_static_headers(self):
        # Formulate the first 5 rows
        return [
            ["#DATA:INV"],
            [
                "#DATA:INV#Myyntilaskujen siirtotiedosto",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            ],
            [
                "TYYPPI0",
                "NUMERO",
                "PVM",
                "ANUMERO",
                "NIMI1",
                "NIMI2",
                "LOSOITE",
                "OSOITE",
                "VIITTEENNE",
                "VIITTEEMME",
                "NETTOPVM",
                "KIELI",
                "VALUUTTA",
                "VKERROIN",
                "SUMMA",
                "LAJI",
                "ALVTAPA",
                "VIESTI",
                "VIITE",
                "MEHTO",
                "ARVOPVM",
                "HYVITYSLASKUNRO",
            ],
            [
                "TYYPPI1",
                "NUMERO",
                "POSITIO",
                "KOODI",
                "NIMIKE",
                "KPL",
                "YKSIKKO",
                "OVH",
                "ALE",
                "MK",
                "TILI",
                "KPAIKKA",
                "JUOKSU",
                "RIVIKOODI",
                "VALUUTTA",
                "ALV",
                "PROJEKTI",
                "TXT",
                "",
                "",
                "",
                "",
                "",
            ],
            ["TYYPPI2", "NUMERO", "TOSITE"],
        ]

    def _prepare_invoice_row(self, invoice):  # noqa: E501
        # Formulate a row that pertains to invoice (i.e. column A is 0)
        partner = invoice.partner_id
        payment_term = (
            invoice.invoice_payment_term_id
            and invoice.invoice_payment_term_id.line_ids
            and invoice.invoice_payment_term_id.line_ids[0]
            or False
        )
        payment_term_nb_days = (
            payment_term.nb_days
            if payment_term and payment_term.delay_type == "days_after"
            else ""
        )
        # TODO raise exception if delay type differs

        return [
            "0",  # A
            invoice.name if invoice.name != "/" else _("DRAFT"),  # B
            invoice.invoice_date.strftime("%m/%d/%Y")
            if invoice.invoice_date
            else "",  # C
            "99999",  # D # TODO what is ANUMERO?
            partner.name or "",  # E
            "",  # F
            f"{partner.street or ''} {partner.street2 or ''}".strip(),  # G
            f"{partner.zip or ''} {partner.city or ''}".strip(),  # H
            invoice.ref or "",  # I
            "",  # J
            (invoice.invoice_date + timedelta(days=payment_term_nb_days)).strftime(
                "%m/%d/%Y"
            ),  # K
            "ENG" if partner.lang == "en_us" else "FIN",  # L
            invoice.currency_id.name or "",  # M
            "1",  # N
            str(invoice.amount_total or ""),  # O
            "5",  # P
            "1",  # Q
            "",  # R
            invoice.payment_reference or "",  # S
            payment_term_nb_days,  # T
            invoice.invoice_date.strftime("%m/%d/%Y")
            if invoice.invoice_date
            else "",  # U
            "0",  # V
        ]

    def _prepare_invoice_line_row(self, invoice, line, running_number):  # noqa: E501
        # Formulate a row that pertains to invoice (i.e. column A is 1)

        # Check if analytic distribution is set
        # TODO validate that only single AA is used
        analytic_account_name = ""
        if line.analytic_distribution and len(list(line.analytic_distribution.keys())):
            analytic_account = (
                self.env["account.analytic.account"]
                .sudo()
                .search(
                    [("id", "=", list(line.analytic_distribution.keys())[0])], limit=1
                )
            )

            analytic_account_name = analytic_account.name

        return [
            "1",  # A
            invoice.name if invoice.name != "/" else _("DRAFT"),  # B
            "",  # C
            line.product_id.default_code or "",  # D
            line.product_id and line.product_id.name or "",  # E
            str(line.quantity or ""),  # F
            line.product_uom_id and line.product_uom_id.name.upper() or "",  # G
            str(line.price_unit or ""),  # H
            line.discount or 0,  # I
            str(line.price_subtotal or ""),  # J
            line.account_id.code or "",  # K
            analytic_account_name,  # L
            running_number,  # M
            "1",  # N
            invoice.currency_id.name or "",  # O
            (
                str(line.tax_ids[0].amount).rstrip("0").rstrip(".")
                if line.tax_ids
                else ""
            ),  # P
            "",  # Q
            line.name or "",  # R
            "",  # S
            "",  # T
            "",  # U
            "",  # V
        ]
