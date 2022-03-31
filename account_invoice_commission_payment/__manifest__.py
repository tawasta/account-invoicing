##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2020 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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

{
    "name": "Account Invoice - Create commission payments from invoices",
    "summary": "Allows Making commission payments from invoices",
    "version": "14.0.1.4.0",
    "category": "Invoicing",
    "website": "https://github.com/Tawasta/account-invoicing",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": ["account", "account_invoice_commission", "account_invoice_margin"],
    "data": [
        "security/ir.model.access.csv",
        # "views/account_move.xml",
        "views/account_move_line.xml",
        "views/account_payment.xml",
        "views/config_settings.xml",
        "views/report_payment_commission.xml",
        "wizards/account_invoice_commission_payment_wizard.xml",
    ],
    "demo": [],
}
