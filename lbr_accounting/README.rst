.. |maturity| image:: https://img.shields.io/badge/maturity-Beta-green.png
    :alt: Beta

.. |badge1| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

.. |badge2| image:: https://raster.shields.io/badge/github-Libreinnova-brightgreen.png?logo=github
    :target: https://github.com/libreinnova/odoo_custom_addons
    :alt: Libreinnova custom addons repository

==============
LBR accounting
==============

|maturity| |badge1| |badge2|

Expansion of the standard accounting module
-------------------------------------------

This module adds various improvements:

* Install third-party accounting technical modules and applications.
* Install third-party SEPA modules by OCA.
* Allow to install AEAT modules in *General Settings > Accounting* page.
* Add accounts verification for correct use of multi-company accounts.
* Add company name to account name.
* Automatically assign journals in trial balance report wizard. You can check **'Not included in trial balance report'** on the journal view.

Contracts
~~~~~~~~~

* Show total in contract tree view.
* Add **contract** accounts verification for correct use of multi-company accounts.
* Show **Create invoices** button without debug mode.
* Do not allow adding partners as followers.

Attention!
~~~~~~~~~~

Make sure than you have ``zeep`` Python module installed.

Third-party resources
~~~~~~~~~~~~~~~~~~~~~

This module needs the following third-party repositories:

* `Odoo Accountant Financial Tools and Utils <https://github.com/OCA/account-financial-tools>`_ by OCA
* `Odoo Spain Localization <https://github.com/OCA/l10n-spain>`_ by OCA
* `Management Information System reports for Odoo <https://github.com/OCA/mis-builder>`_ by OCA

Author
------

Developer: Libreinnova, info@libreinnova.com

Contributors
~~~~~~~~~~~~

* Libreinnova
* Pavel Smirnov, pavel@libreinnova.com

Maintainer
~~~~~~~~~~

This module is maintained by Libreinnova, https://libreinnova.com

.. image:: https://libreinnova.com/images/logo.png
   :alt: Libreinnova
   :target: https://libreinnova.com

Disclaimer of Warranties
------------------------

We provide this module as is, and we make no promises or guarantees about this correct working.

We provides this application without warranty of any kind.

We does not warrant that the module will meet your requirements;
that the current application will be uninterrupted, timely, secure, or error-free or that any defects or errors will be corrected.

-------------

Copyright(c): 2021 Libreinnova (https://libreinnova.com/)

All Rights Reserved
