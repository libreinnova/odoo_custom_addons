###############################################################################
#
# Copyright(c): 2019 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# All Rights Reserved
#
###############################################################################
{
    'name': 'LBR accounting',
    'version': '1.0',
    'summary': 'Expansion of the standard accounting module',
    'description': '',
    'category': 'Accounting',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'account',
        'account_balance_line'
    ],
    'data': [
        'views/res_config_settings.xml',
    ],
    'installable': True,
    'application': False,
}