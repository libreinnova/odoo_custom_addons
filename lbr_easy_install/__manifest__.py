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
    'category': 'Tools',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'account',
        'analytic',
        'barcodes',
        'board',
        'calendar',
        'contacts',
        'crm',
        'google_drive',
        'hr_attendance',
        'hr_holidays',
        'l10n_es',
        'mail',
        'maintenance',
        'mass_mailing',
        'mrp',
        'note',
        'payment',
        'product',
        'project',
        'sale_management',
        'stock',
        'web_favicon'
    ],
    'data': [],
    'installable': True,
    'application': False,
}
