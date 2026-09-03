##############################################################################
#
#    Author: Futural Oy
#    Copyright 2026 Futural Oy (https://futural.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/lgpl.html
#
##############################################################################

{
    "name": "Import/Export invoices as Finvoice: Attachment Upload Patch",
    "summary": "Prevent PDF/XML invoice attachment upload crashing (temporary fix)",
    "version": "19.0.1.0.0",
    "category": "Invoicing",
    "website": "https://github.com/tawasta/account-invoicing",
    "author": "Futural",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": ["account_edi_finvoice"],
    "data": [],
    "demo": [],
}
