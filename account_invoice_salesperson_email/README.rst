.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================================================
Account Invoice Salesperson Email to Invoice note
=================================================

When an invoice is created from Sale Order, the invoice's note-field is appended
with the Salesperson's email-address. This module also has an onchange-method
depending on Salesperson, so that the original comment is preserved and only a
new email-address is changed.

Configuration
=============
No special configuration necessary.

Usage
=====
Go to Sale Order and create and Invoice. The created invoice has
Salesperson's email-address if it has been set.

Known issues / Roadmap
======================
There are no known issues with this module.

Credits
=======

Contributors
------------

* Aleksi Savijoki <aleksi.savijoki@tawasta.fi>
* Timo Kekäläinen <timo.kekalainen@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
