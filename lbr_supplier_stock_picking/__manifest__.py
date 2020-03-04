###############################################################################
#
# Copyright(c): 2019 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# All Rights Reserved
#
###############################################################################
{
    'name': 'LBR supplier stock picking',
    'version': '1.0',
    'summary': 'Adds invoice date and number to supplier invoices',
    'description': '',
    'category': 'Tools',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'account'
    ],
    'data': [
        'views/stock_picking.xml'
    ],
    'installable': True,
    'application': False,
}
