from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_om_account_accountant = fields.Boolean(
        string='Odoo12 Accounting (by Odoo Mates & Odoo SA)',
        help='Accounting Reports, Asset Management and Account Budget For Odoo12 Community Edition')

    module_l10n_es_account_bank_statement_import_n43 = fields.Boolean(
        string='Import of Spanish bank statements (Rule 43)',
        help='Click here to install this module '
             '(by Spanish Localization Team, Tecnativa, Odoo Community Association (OCA))')

    module_l10n_es_aeat_mod111 = fields.Boolean(
        string='AEAT 111 model',
        help='Click here to install this module '
             '(by AvanzOSC, RGB Consulting SL, Tecnativa, Odoo Community Association (OCA))')

    module_l10n_es_aeat_mod115 = fields.Boolean(
        string='AEAT 115 model',
        help='Click here to install this module '
             '(by AvanzOSC, Tecnativa, Odoo Community Association (OCA))')

    module_l10n_es_aeat_mod123 = fields.Boolean(
        string='AEAT 123 model',
        help='Click here to install this module '
             '(by Tecnativa, Spanish Localization Team, Odoo Community Association (OCA))')

    module_l10n_es_aeat_mod216 = fields.Boolean(
        string='AEAT 216 model',
        help='Click here to install this module '
             '(by AvanzOSC, Tecnativa, Odoo Community Association (OCA))')

    module_l10n_es_aeat_mod303 = fields.Boolean(
        string='AEAT 303 model',
        help='Click here to install this module '
             '(by Guadaltech, AvanzOSC, Tecnativa, Eficent, Odoo Community Association (OCA))')

    module_l10n_es_aeat_mod347 = fields.Boolean(
        string='AEAT 347 model',
        help='Click here to install this module '
             '(by Tecnativa, PESOL, Odoo Community Association (OCA))')

    module_l10n_es_aeat_mod349 = fields.Boolean(
        string='AEAT 349 model',
        help='Click here to install this module '
             '(by Tecnativa, Eficent, Odoo Community Association (OCA))')

    module_l10n_es_aeat_mod390 = fields.Boolean(
        string='AEAT 390 model',
        help='Click here to install this module '
             '(by Tecnativa, Odoo Community Association (OCA))')

    module_l10n_es_aeat_sii = fields.Boolean(
        string='Immediate Supply of Information on VAT (SII)',
        help='Click here to install this module '
             '(by Acysos S.L., Diagram, Minorisa, Studio73, FactorLibre, Comunitea, Otherway, Tecnativa, '
             'Javi Melendez, Odoo Community Association (OCA))')
