from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    journal_id = fields.Many2one(required=False)

    @api.multi
    def name_get(self):
        # Set default type for invoice which was created by incoming email server
        if self._context.get('fetchmail_server_id'):
            for inv in self:
                if not inv.type:
                    inv.type = 'in_invoice'
        return super(AccountInvoice, self).name_get()
