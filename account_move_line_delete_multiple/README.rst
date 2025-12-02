.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==========================================
Vendor Bills: Delete lines with checkboxes
==========================================

**Odoo** add-on that lets you quickly remove lines from *draft* vendor bills
using simple checkboxes in the invoice line tree.

- Works on **Vendor Bills**, **Vendor Credit Notes (Refunds)** and **Vendor Receipts**
  (``in_invoice``, ``in_refund``, ``in_receipt``).
- Only affects normal **product lines**, **section** and **note** rows
  (never tax/analytic/other technical rows).
- The deletion is executed immediately when the checkbox value is saved.

Installation
============
* Just install this module

Configuration
=============

Usage
=====

1. Open a **Vendor Bill** (or Vendor Credit Note / Vendor Receipt) in **Draft** state.  
2. In the **Invoice Lines** section, you will see a new column **Select**.  
3. Tick the checkbox on any line you wish to delete.  
4. Click **Save** — the marked lines will be automatically deleted.  

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
