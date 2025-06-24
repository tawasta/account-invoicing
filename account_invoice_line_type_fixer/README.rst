.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

================================
Fix types for account move lines
================================

This module is meant to be used after an odoo installation migration
to fix invoice lines, which have a wrong type.

Configuration
=============
\-

Usage
=====
Go to Server Actions and select a range for years to recompute account move lines.
Set the account ID that is linked to these account move lines.


For example one can run:

records.account_move_line_type_fixer(2017, 2025, 100)

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Timo Kekäläinen <timo.kekalainen@tawasta.fi>
* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: http://tawasta.fi/

This module is maintained by Futural Oy
