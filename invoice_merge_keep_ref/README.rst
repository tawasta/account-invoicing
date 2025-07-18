.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
        :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
        :alt: License: AGPL-3

==============================
Invoice Merge - Keep Ref Field
==============================

This module extends the functionality of the **Invoice Merge** wizard by introducing an option to **preserve the "ref" field** values from the original invoices when merging them.

When enabled, the customer references (`ref`) from all merged invoices will be collected and copied to the resulting invoice's `ref` field.

Configuration
=============
No configuration is required.

Usage
=====
1. Select multiple draft invoices belonging to the same partner.
2. Click "Action" → "Merge Partner Invoice".
3. In the wizard, enable the checkbox **Keep customer references**.
4. Complete the merge as usual.
5. The resulting invoice's `ref` field will contain all non-empty original references.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
        :alt: Futural Oy
        :target: http://tawasta.fi/

This module is maintained by Futural Oy
