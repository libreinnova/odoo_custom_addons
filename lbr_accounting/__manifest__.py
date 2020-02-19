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
        'account_balance_line',
        'account_cancel',
        'account_chart_update',
        'account_coa_menu',
        'account_payment_partner',
        'contract',
        'l10n_es_account_asset',
        'l10n_es_aeat',
        'l10n_es_mis_report',
        'l10n_es_vat_book'
    ],
    'data': [
        'views/account_invoice.xml',
        'views/account_move_line.xml',
        'views/contract_contract.xml',
        'views/res_config_settings.xml',
    ],
    'external_dependencies': {
        'python': [
            'zeep',
        ]
    },
    'installable': True,
    'application': False,
}
