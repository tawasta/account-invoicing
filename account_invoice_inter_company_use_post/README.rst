.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================================
Use _post -method in Intercompany invoice creation
==================================================

Enable to create Intercompany invoices in invoice tree view with 'Post entries'
action. The same lines of code is used under _post -method which are used
originally under action_post -method. This is done by first importing the lines
of code in string format, then manipulating this string and finally running it.

Configuration
=============
Intercompany invoicing is needed to be in use

Usage
=====
Select an invoice that is expected to create an intercompany invoice.
See how account_invoice_inter_company module is meant to be used.

Known issues / Roadmap
======================
The imported lines of code is expected to be syntactically valid

Credits
=======

Contributors
------------

* Timo Kekäläinen <timo.kekalainen@tawasta.fi>
* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
