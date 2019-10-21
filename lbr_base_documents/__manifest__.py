###############################################################################
#
# Copyright(c): 2019 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# All Rights Reserved
#
###############################################################################
{
    'name': 'LBR base documents',
    'version': '1.0',
    'summary': 'One-click install of document management system',
    'description': '',
    'category': 'Document Management',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'muk_dms',
        'muk_dms_actions',
        'muk_dms_file',
        'muk_dms_lobject',
        'muk_dms_mail',
        'muk_dms_view',
    ],
    'data': [
        'templates/assets.xml'
    ],
    'installable': True,
    'application': False,
}
