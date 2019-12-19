from odoo import api, fields, models


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
