##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2023- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import _, fields, models
from odoo.exceptions import UserError

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class AccountMove(models.Model):
    # 1. Private attributes
    _inherit = "account.move"

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    def _post(self, soft=True):
        """Post/Validate the documents."""
        if soft:
            future_moves = self.filtered(
                lambda move: move.date > fields.Date.context_today(self)
            )
            to_post = self - future_moves
        else:
            to_post = self
        self._check_invoice_payment_term(to_post)
        return super(AccountMove, self)._post(soft)

    # 8. Business methods
    def _check_invoice_payment_term(self, to_post):
        for record in to_post:
            if record.move_type == "out_invoice" and not record.invoice_payment_term_id:
                raise UserError(_("Please set a payment term before validating."))
