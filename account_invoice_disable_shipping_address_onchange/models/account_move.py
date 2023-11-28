from odoo import api

from odoo.addons.account.models.account_move import AccountMove
from odoo.addons.sale.models.account_invoice import AccountMove as SaleAccountMove


@api.onchange("partner_id")
def _onchange_partner_id(self):
    return AccountMove._onchange_partner_id(self)


SaleAccountMove._onchange_partner_id = _onchange_partner_id
