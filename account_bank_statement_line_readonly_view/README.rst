.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==========================================
Account Bank Statement Lines Readonly View
==========================================

* Adds a readonly view for bank statement lines that is accessible by accounting users
* Shows lines' reconciliation info but does not allow doing reconciliation directly from this view
* Intended for easier debugging and viewing of multiple bank statements' contents
* The views are based on the views of OCA's account_statement_base, as Odoo 17
  Community has no views for bank statement lines

Configuration
=============
\-

Usage
=====
* Navigate to Accounting -> Journals -> Bank Statement Lines
* The lines can not be created, edited or deleted, and the reconciliation can not be reverted from the view

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@tawasta.fi>
* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
