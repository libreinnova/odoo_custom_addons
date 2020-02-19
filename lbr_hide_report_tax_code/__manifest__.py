###############################################################################
#
# Copyright(c): 2020 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# All Rights Reserved
#
###############################################################################
{
    'name': 'LBR hide report tax code',
    'version': '1.0',
    'summary': 'Remove the tax code of the report lines',
    'description': '',
    'category': 'Reporting',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'account',
        'sale'
    ],
    'data': [
        'report/account_invoice.xml',
        'report/sale_order.xml'
    ],
    'installable': True,
    'application': False,
}
