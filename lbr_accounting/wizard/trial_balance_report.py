from odoo import api, fields, models, _


class TrialBalanceReportWizard(models.TransientModel):
    _inherit = 'trial.balance.report.wizard'

    journal_ids = fields.Many2many(default=lambda self: self.get_balance_journal_ids())

    @api.model
    def get_balance_journal_ids(self):
        return self.env['account.journal'].search([
            ('not_in_trial_balance_report', '=', False),
            ('company_id', '=', self.env.user.company_id.id)
        ])
