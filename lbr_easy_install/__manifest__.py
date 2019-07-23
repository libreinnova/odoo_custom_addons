###############################################################################
#
# Copyright(c): 2019 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# All Rights Reserved
#
###############################################################################
{
    'name': 'LBR easy install',
    'version': '1.0',
    'summary': 'One-click install of base Odoo modules',
    'description': '',
    'category': 'Inventory',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'account',
        'analytic',
        'barcodes',
        'calendar',
        'contacts',
        'crm',
        'google_drive',
        'hr_attendance',
        'l10n_es',
        'mail',
        'mass_mailing',
        'note',
        'payment',
        'product',
        'project',
        'sale_management',
        'stock'
    ],
    'data': [],
    'installable': True,
    'application': False,
}
