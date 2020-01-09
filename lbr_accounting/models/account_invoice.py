from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


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

    @api.multi
    def action_invoice_verify_accounts(self):
        cid = self.company_id.id
        message = ''

        def return_message(element, company_name):
            message_pattern = _("The invoice's %s isn't correct (it belongs to '%s').\n")
            return _(message_pattern % (element, company_name))

        # We need to use sudo() for check other company data
        self = self.sudo()
        # Check payment term
        if self.payment_term_id and self.payment_term_id.company_id.id != cid:
            message += return_message(_('payment term'), self.payment_term_id.company_id.name)
        # Check journal
        if self.journal_id and self.journal_id.company_id.id != cid:
            message += return_message(_('journal'), self.journal_id.company_id.name)
        # Check account
        if self.account_id and self.account_id.company_id.id != cid:
            message += return_message(_('account'), self.account_id.company_id.name)
        # Check fiscal position
        if self.fiscal_position_id and self.fiscal_position_id.company_id.id != cid:
            message += return_message(_('fiscal position'), self.fiscal_position_id.company_id.name)
        # Check partner bank
        if self.partner_bank_id and self.partner_bank_id.company_id.id != cid:
            message += return_message(_('partner bank'), self.partner_bank_id.company_id.name)
        # Check invoice lines
        for line in self.invoice_line_ids:
            # Check line account
            if line.account_id and line.account_id.company_id.id != cid:
                message += return_message(_('line [%s] account') % line.name, line.account_id.company_id.name)
            # Check line analytic account
            if line.account_analytic_id and line.account_analytic_id.company_id.id != cid:
                message += return_message(_('line [%s] analytic account') % line.name,
                                          line.account_analytic_id.company_id.name)
            # Check line asset
            if line.asset_id and line.asset_id.company_id.id != cid:
                message += return_message(_('line [%s] asset') % line.name, line.asset_id.company_id.name)
            # Check line taxes
            for tax in line.invoice_line_tax_ids:
                if tax.company_id.id != cid:
                    message += return_message(_('line [%s] tax [%s]') % (line.name, tax.name), tax.company_id.name)

        # Return result message in case of any error
        if len(message):
            message_summary_pattern = _("\nYou need to use parameters of '%s' company.")
            message += message_summary_pattern % self.company_id.name
            raise ValidationError(message)
