from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ContractContract(models.Model):
    _inherit = 'contract.contract'

    amount_total = fields.Float('Amount total', compute='_compute_amount_total', store=True)

    @api.one
    @api.depends('contract_line_ids.price_subtotal')
    def _compute_amount_total(self):
        amount_total = 0
        for line in self.contract_line_ids:
            amount_total += line.price_subtotal
        self.amount_total = amount_total

    @api.multi
    def action_contract_verify_accounts(self):
        cid = self.company_id.id
        message = ''

        def return_message(element, company_name):
            message_pattern = _("The contract's %s isn't correct (it belongs to '%s').\n")
            return _(message_pattern % (element, company_name))

        # We need to use sudo() for check other company data
        self = self.sudo()
        # Check payment mode
        if self.payment_mode_id and self.payment_mode_id.company_id.id != cid:
            message += return_message(_('payment mode'), self.payment_mode_id.company_id.name)
        # Check journal
        if self.journal_id and self.journal_id.company_id.id != cid:
            message += return_message(_('journal'), self.journal_id.company_id.name)
        # Check fiscal position
        if self.fiscal_position_id and self.fiscal_position_id.company_id.id != cid:
            message += return_message(_('fiscal position'), self.fiscal_position_id.company_id.name)
        # Check group
        if self.group_id and self.group_id.company_id.id != cid:
            message += return_message(_('group'), self.group_id.company_id.name)
        # Check contract lines
        for line in self.contract_line_ids:
            # Check line analytic account
            if line.analytic_account_id and line.analytic_account_id.company_id.id != cid:
                message += return_message(_('line [%s] analytic account') % line.name,
                                          line.analytic_account_id.company_id.name)

        # Return result message in case of any error
        if len(message):
            message_summary_pattern = _("\nYou need to use parameters of '%s' company.")
            message += message_summary_pattern % self.company_id.name
            raise ValidationError(message)
