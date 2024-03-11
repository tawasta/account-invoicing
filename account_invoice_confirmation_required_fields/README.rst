.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========================================
Invoice Confirmation: Check Required Fields
===========================================

* Prevents customer invoice confirmation if certain fields are not filled in.
* Required fields are configurable in accounting options
* Currently supports checking of 
  * email of the partner
  * street, zip, city and country of the partner
  * street, zip, city and country of the shipping address

Configuration
=============
* In invoicing settings, set which confirmation checks you want to enforce

Usage
=====
* After configuration, attempt to confirm a customer invoice with some
  empty required fields, and you will get an error message.

Known issues / Roadmap
======================
* Add more configurable fields to the module as needed
* Consider adding support for also other types of invoices

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
