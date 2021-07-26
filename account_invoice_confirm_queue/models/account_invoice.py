from odoo import api
from odoo import models
from odoo.addons.queue_job.job import job


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @job()
    @api.multi
    def action_invoice_open_queued(self):
        self.ensure_one()
        self.action_invoice_open()
