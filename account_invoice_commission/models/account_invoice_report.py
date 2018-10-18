# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountInvoiceReport(models.Model):
	_inherit = 'account.invoice.report'

	commission_paid = fields.Boolean(
		string='Commission paid',
		default=False,)