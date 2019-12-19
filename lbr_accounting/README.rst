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
* Allow to expand the accounting module with `Odoo 12 Accounting <https://www.odoo.com/apps/modules/12.0/om_account_accountant/>`_ by Odoo Mates, Odoo SA.
* Contain Spanish translation for this module.
* Install third-party technical modules y applications.
* Set default type for **invoice** which was created by incoming email server.
* Allow to install AEAT modules in *General Settings > Accounting* page.
* Show total in contract tree view.

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

Third-party resources
~~~~~~~~~~~~~~~~~~~~~

This module needs the following third-party modules:

* `Odoo 12 Accounting <https://www.odoo.com/apps/modules/12.0/om_account_accountant/>`_ by Odoo Mates, Odoo SA.
* `Odoo 12 Accounting PDF Reports <https://www.odoo.com/apps/modules/12.0/accounting_pdf_reports/>`_ by Odoo Mates, Odoo SA.
* `Odoo 12 Assets Management <https://www.odoo.com/apps/modules/12.0/om_account_asset/>`_ by Odoo Mates, Odoo SA.
* `Odoo 12 Budget Management <https://www.odoo.com/apps/modules/12.0/om_account_budget/>`_ by Odoo Mates, Odoo SA.

Disclaimer of Warranties
------------------------

We provide this module as is, and we make no promises or guarantees about this correct working.

We provides this application without warranty of any kind.

We does not warrant that the module will meet your requirements;
that the current application will be uninterrupted, timely, secure, or error-free or that any defects or errors will be corrected.

-------------

Copyright(c): 2019 Libreinnova (https://libreinnova.com/)

All Rights Reserved
