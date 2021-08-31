###############################################################################
#
# Copyright(c): 2021 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# All Rights Reserved
#
###############################################################################
{
    'name': 'LBR partner search by VAT',
    'version': '1.0',
    'summary': 'Allows to search contacts by VAT code',
    'description': '',
    'category': 'Tools',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'base',
    ],
    'data': [
        'views/res_partner.xml'
    ],
    'installable': True,
    'application': False,
}
