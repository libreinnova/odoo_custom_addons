from odoo import api, fields, models, _


class AccountAccount(models.Model):
    _inherit = 'account.account'
    _rec_name = 'display_name'

    display_name = fields.Char('Display name', compute='compute_display_name')

    @api.depends('company_id', 'name', 'code')
    def compute_display_name(self):
        is_multi_company = True if self.env['res.company'].search_count([]) > 1 else False
        for account in self:
            account_name = '%s %s' % (account.code, account.name)
            # Add company name to the account name
            if is_multi_company and account.company_id:
                account_name += ' [%s]' % account.company_id.name
            account.display_name = account_name
