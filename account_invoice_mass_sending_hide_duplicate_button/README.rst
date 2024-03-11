.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================================================
Account Invoice Mass Sending: Hide duplicate button
===================================================

* OCA's account_invoice_mass_sending adds a new button to the invoice Send and Print
  wizard, that triggers the submission using jobs. However, the module still leaves 
  the core's submission button in place. 
* This module hides the core button, so only the job-based sending is available.
  The OCA button text is renamed to "Send (via Job Queue)" to better fit both single
  and batch invoice sending.

Configuration
=============
* None needed

Usage
=====
* Go to either a) invoice list, select some invoices and click Action --> Print & Send, or 
  b) invoice form view, and click Print & Send. 
* Only a single sending button labeled "Send (via Job Queue)" is visible.

Known issues / Roadmap
======================
* None

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
