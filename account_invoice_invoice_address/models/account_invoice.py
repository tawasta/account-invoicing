# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class AccountInvoice(models.Model):

    # 1. Private attributes
    _inherit = 'account.invoice'

    # 2. Fields declaration
    partner_invoice_id = fields.Many2one('res.partner', string='Invoicing address')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods
    @api.model
    def create(self, vals):
        if 'partner_id' in vals and 'partner_invoice_id' in vals and not vals['partner_invoice_id']:
            vals['partner_invoice_id'] = vals['partner_id']

        return super(AccountInvoice, self).create(vals)

    @api.multi
    def write(self, vals):
        for record in self:
            if 'partner_id' in vals and 'partner_invoice_id' not in vals:
                vals['partner_invoice_id'] = vals['partner_id']

            elif 'partner_invoice_id' not in vals and not record.partner_invoice_id and record.partner_id:
                vals['partner_invoice_id'] = record.partner_id.id

            elif 'partner_invoice_id' in vals and not vals['partner_invoice_id'] and record.partner_id:
                vals['partner_invoice_id'] = record.partner_id.id

        return super(AccountInvoice, self).write(vals)

    # 7. Action methods

    # 8. Business methods
    @api.model
    def _init_invoicing_address(self):
        invoices = self.search([('partner_invoice_id', '=', False)])

        for invoice in invoices:
            # This check should be obsolete due to the search filter
            if invoice.partner_invoice_id:
                continue

            invoice.partner_invoice_id = invoice.partner_id