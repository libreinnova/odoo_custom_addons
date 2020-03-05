###############################################################################
#
# Copyright(c): 2020 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# All Rights Reserved
#
###############################################################################
{
    'name': 'LBR supplier stock picking',
    'version': '1.0',
    'summary': 'Suppliers stock picking date and number',
    'description': '',
    'category': 'Stock',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'stock'
    ],
    'data': [
        'views/stock_picking.xml'
    ],
    'installable': True,
    'application': False,
}
