.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

================================
Account Reverse Carry Ref & User
================================
This module extends Odoo's invoice reversal process.  
When creating a refund or using the **Modify** option (which generates both a credit note and a new invoice),
it automatically carries over key information from the original invoice to the new move(s).  

Specifically, it ensures that:
* The **invoice reference** (``ref``)  
* The **salesperson** (``invoice_user_id``)  

are retained on the resulting invoices after reversal.  
This helps maintain consistent invoice metadata and accountability without manual re-entry.

Installation
============
* Just install this module

Configuration
=============
* No configuration required.

Usage
=====
* When using **Reverse → Refund** or **Reverse → Modify** on any posted invoice,
  this module automatically copies the following fields from the original invoice
  to the newly created move(s):

  * ``ref`` – Vendor or internal reference  
  * ``invoice_user_id`` – Salesperson

* Works transparently for both *customer* and *vendor* invoices.
* The carryover happens inside the inherited ``reverse_moves`` method, so it applies
  to both Refund and Modify flows.
* If multiple invoices are reversed at once, they are paired deterministically by ID.

Known issues / Roadmap
======================
* None

Credits
=======

Contributors
------------
* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
