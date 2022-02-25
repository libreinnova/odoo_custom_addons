###############################################################################
#
# Copyright(c): 2022 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# All Rights Reserved
#
###############################################################################
{
    'name': 'LBR Weekdays',
    'version': '1.0',
    'summary': 'Helper weekdays model',
    'description': '',
    'category': 'Tools',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'base'
    ],
    'data': [
        'data/weekday.xml',
        'security/ir.model.access.csv',
        'views/weekday.xml'
    ],
    'installable': True,
    'application': False,
}
