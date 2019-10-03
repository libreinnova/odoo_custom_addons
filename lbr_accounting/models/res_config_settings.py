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
