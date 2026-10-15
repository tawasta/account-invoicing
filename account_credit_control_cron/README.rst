.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========================
Account Credit Control Cron
===========================

* Automates the manual Credit Control run (Accounting > Credit Control >
  Runs) as a daily scheduled action, for every company that has credit
  control policies configured.
* Each day it performs the same steps a user would do by hand: create a
  run for today, generate the credit control lines, mark them ready, then
  run the channel action - which sends the email reminders in the
  background. Letter-channel lines are left "To Do" for manual printing,
  exactly like a manual run leaves them.
* A company is skipped for the day if a run for that date already exists,
  so re-running the cron never creates duplicate runs or reminders.
* A failure for one company (e.g. a misconfigured policy) is logged and
  does not prevent other companies from being processed.

Configuration
=============
* The scheduled action ("Credit Control: Run daily reminders", Settings >
  Technical > Scheduled Actions) is installed **inactive**. Activate it,
  and adjust the time of day it runs, once you are ready to switch from
  manual to automatic runs.
* Each company must have at least one Credit Control Policy configured
  (Accounting > Configuration > Credit Control > Policies) - a company
  with none configured is silently skipped by the cron.

Usage
=====
* Once activated, no further action is needed - the cron runs daily and
  behaves exactly like the manual "Runs" workflow.

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

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
