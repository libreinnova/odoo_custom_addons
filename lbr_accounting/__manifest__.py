###############################################################################
#
# Copyright(c): 2021 Libreinnova (<https://libreinnova.com/>)
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
        'account_chart_update',
        'account_financial_report',
        'account_lock_date_update',
        'account_payment_partner',
        'account_banking_sepa_credit_transfer',
        'account_banking_sepa_direct_debit',
        'contract_payment_mode',
        'l10n_es_account_asset',
        'l10n_es_aeat_mod190',
        'l10n_es_mis_report',
        'l10n_es_vat_book',
    ],
    'data': [
        'views/account_journal.xml',
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
