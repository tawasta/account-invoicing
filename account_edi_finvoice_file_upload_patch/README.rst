.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

===========================================================
Import/Export invoices as Finvoice: Attachment Upload Patch
===========================================================

* Prevent PDF/XML invoice attachment upload crashing
* Temporary fix as a separate module until lands on OCA `account_edi_finvoice`

Configuration
=============

* None

Usage
=====

* Upload a PDF or a Finvoice 3.0 XML from the vendor bills list view.

Known issues / Roadmap
======================

* Remove this module once `account_edi_finvoice` itself patched in
  https://github.com/OCA/l10n-finland.

Credits
=======

Contributors
------------
* Timo Talvitie <timo.talvitie@futural.fi>
