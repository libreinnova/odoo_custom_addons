###############################################################################
#
# Copyright(c): 2021 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# All Rights Reserved
#
###############################################################################
{
    'name': 'LBR order help title',
    'version': '1.0',
    'summary': 'Show help-information order title',
    'description': '',
    'category': 'Sale',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'purchase',
        'sale'
    ],
    'data': [
        'views/purchase_order.xml',
        'views/sale_order.xml'
    ],
    'installable': True,
    'application': False,
}
