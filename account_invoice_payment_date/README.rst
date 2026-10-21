.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================
Payment date for invoices
=========================

Save the date when invoice was fully paid

* The payment date is the latest date of the payments reconciled with the invoice.
  It is saved only when all of the payments are matched with a bank statement.
* An invoice that has been marked as paid with an accounting entry gets the
  latest date of the counterpart entries.
* A scheduled action ("Invoice: Compute payment date") fills the date daily
  for paid invoices that do not have it yet.

Configuration
=============
\-

Usage
=====
* The payment date is shown on the invoice form, and as an optional column
  in the invoice list.
* The invoices can be searched and filtered by the payment date.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>
* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
