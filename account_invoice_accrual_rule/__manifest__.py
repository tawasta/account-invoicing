##############################################################################
#
#    Author: Futural Oy
#    Copyright 2024 Futural Oy (https://futural.fi)
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
    "name": "Invoice accrual rules",
    "summary": "Add accrual rules to invoices",
    "version": "17.0.1.0.1",
    "category": "Sales",
    "website": "https://github.com/tawasta/account-invoicing",
    "author": "Futural",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "auto_install": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "account",
        "product",
    ],
    "data": [
        "security/model_access.xml",
        "views/account_move.xml",
        "views/accrual_rule.xml",
        "views/product_template.xml",
    ],
    "assets": {},
    "demo": [],
}
