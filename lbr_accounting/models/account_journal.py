from odoo import api, fields, models, _


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    not_in_trial_balance_report = fields.Boolean('Not included in trial balance report')
