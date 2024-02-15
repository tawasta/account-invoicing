from odoo import SUPERUSER_ID, api


def post_init_hook(cr, _):
    env = api.Environment(cr, SUPERUSER_ID, {})

    payments = env["account.payment"].sudo().search([])
    payments._compute_ref_invoice_id()
