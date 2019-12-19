.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==========================
Notice period for Invoices
==========================

* Enables setting informative notice periods for customers as well as
  individual invoices

Configuration
=============

* Set the default notice period in Accounting -> Configuration -> Settings
* Optional: define custom notice period for specific partners in Sales
  -> Customers

Usage
=====

* Create a new invoice. If a partner has a custom notice period, that one is
  suggested. Otherwise, the default one is suggested.

Known issues / Roadmap
======================

* Note that this module only provides an extra field to be used with PDF 
  prints, accounting integrations etc. It has no functionality related to e.g. 
  creating reminder invoices with increased totals, if the original invoice was
  not paid in time.

Credits
=======

Contributors
------------
* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>
* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: https://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: https://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.