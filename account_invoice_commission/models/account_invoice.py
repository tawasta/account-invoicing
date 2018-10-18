# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountInvoice(models.Model):
	_inherit = 'account.invoice'

	commission_paid = fields.Boolean(
		string='Commission paid',
		default=False,)