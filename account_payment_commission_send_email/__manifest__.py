##############################################################################
#
#    Author: Jarmo Kortetjärvi
#    Copyright 2015 Futural Oy (https://futural.fi)
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
    "name": "Account payment commission send email",
    "summary": "Allows sending a payment summary by email",
    "version": "17.0.1.0.1",
    "category": "Accounting & Finance",
    "website": "https://github.com/tawasta/account-invoicing",
    "author": "Futural",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["account", "account_invoice_commission_payment"],
    "data": [
        "data/mail_template_data.xml",
        "views/account_payment.xml",
    ],
}
