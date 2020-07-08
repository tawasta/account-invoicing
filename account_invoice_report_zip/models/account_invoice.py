import base64
import os
import shutil
import zipfile
from random import randrange

from odoo import api, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.multi
    def to_zip(self, records, archive_name):
        archive_path = "/tmp/{}.{}".format(
            archive_name,
            "zip",
        )

            for record in records:
                file_name = "{} - {} - {}.{}".format(
                    record._get_report_base_filename(),
                    record.id,
                    record.name,
                    "pdf"
                )

                pdf_file = self.env.ref("account.account_invoices")\
                    .sudo().render_qweb_pdf([record.id])

                zip_archive.writestr(
                    file_name,
                    data=pdf_file[0],
                )


        archive_filename = "{}.{}".format(
            archive_name,
            "zip",
        )


        f = open(archive_path, 'rb')
        archive_attachment = self.env["ir.attachment"].sudo().create({
            "name": archive_filename,
            "display_name": archive_filename,
            "res_name": archive_filename,
            "public": False,
            "datas_fname": archive_filename,
            "datas": base64.b64encode(f.read()),
            "type": "binary",
        })
        f.close()

        return {
            "type": "ir.actions.act_url",
            "url": archive_attachment.local_url,
        }
