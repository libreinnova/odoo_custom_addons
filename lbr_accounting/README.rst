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

* Modify *General Settings > Accounting* page.
* Install third-party accounting technical modules and applications.
* Install third-party SEPA modules by OCA.
* Set default type for **invoice** which was created by incoming email server.
* Allow to install AEAT modules in *General Settings > Accounting* page.
* Add **invoice** accounts verification for correct use of multi-company accounts.
* Add account invoice line tree view for customers.
* Add company name to account name.
* Fix compute rounding on AEAT mod190 report.
* Show **Allow Cancelling Entries** field on journals without debug mode (only account managers).
* Automatically assign journals in trial balance report wizard. You can check **'Not included in trial balance report'** on the journal view.

Contracts
~~~~~~~~~

* Show total in contract tree view.
* Add **contract** accounts verification for correct use of multi-company accounts.
* Show **Create invoices** button without debug mode.

.. Allow to expand the accounting module with `Odoo 12 Accounting <https://www.odoo.com/apps/modules/12.0/om_account_accountant/>`_ by Odoo Mates, Odoo SA.
.. Contain Spanish translation for this module.

Attention!
~~~~~~~~~~

Make sure than you have ``zeep`` Python module installed.

To install
~~~~~~~~~~

This module installs third-party several applications and technical modules:

.. list-table::
    :header-rows: 0

    * - `account_balance_line <https://www.odoo.com/apps/modules/12.0/account_balance_line/>`_
      - Balance on journal items
      - This module adds a balance total for lines in move line view.
    * - `account_coa_menu <https://www.odoo.com/apps/modules/12.0/account_coa_menu/>`_
      - Chart of Accounts Menus
      - This module adds menu entries Chart of Accounts and all it sub menus.
    * - `l10n_es_aeat <https://www.odoo.com/apps/modules/12.0/l10n_es_aeat/>`_
      - AEAT base
      - Base module for AEAT statements. Requires *account_tax_balance* and *date_range* modules.
    * - `l10n_es_account_asset <https://github.com/OCA/l10n-spain/tree/12.0/l10n_es_account_asset/>`_
      - Gestión de activos fijos para España
      - Cambia la gestión estándar de activos fijos de Odoo para acomodarla a las regulaciones españolas.

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

Third-party resources
~~~~~~~~~~~~~~~~~~~~~

This module needs the following third-party repositories:

* `Odoo Accountant Financial Tools and Utils <https://github.com/OCA/account-financial-tools>`_ by OCA
* `Odoo Spain Localization <https://github.com/OCA/l10n-spain>`_ by OCA
* `Management Information System reports for Odoo <https://github.com/OCA/mis-builder>`_ by OCA

Disclaimer of Warranties
------------------------

We provide this module as is, and we make no promises or guarantees about this correct working.

We provides this application without warranty of any kind.

We does not warrant that the module will meet your requirements;
that the current application will be uninterrupted, timely, secure, or error-free or that any defects or errors will be corrected.

-------------

Copyright(c): 2019 Libreinnova (https://libreinnova.com/)

All Rights Reserved
