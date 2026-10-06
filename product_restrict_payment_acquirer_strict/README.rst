.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============================================
Product Restrict Payment Acquirer - Strict mode
===============================================

* Adds an "All Products (strict)" option to the payment provider restriction
  mode of the OCA module ``product_restrict_payment_acquirer``.
* Only payment providers allowed by every restricted product in the sale order
  are offered. Order lines with no allowed payment provider restrictions set 
  are ignored. 
* If the products have no payment provider in common, no payment option is
  offered and the order cannot be paid online.
* The other modes of ``product_restrict_payment_acquirer`` work as before.

Configuration
=============
* Go to Settings > Sales > Payment Acquirer Restriction and select the new
  "All Products (strict)" mode.
* Set "Allowed Payment Providers" on the Sales tab of the products that should
  be restricted.

Usage
=====
* Proceed to cart in e-commerce. Payment providers that are not supported 
  by all products in the cart are not shown to the visitor.

Known issues / Roadmap
======================
* Note that this module and its OCA parent do similar things as
  ``website_sale_limit_payment_providers`` (see Futural e-commerce repo)
  but without the dependencies that deal with sale orders getting split to 
  multiple companies. So consider this a lighter alternative.

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
