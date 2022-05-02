from odoo import api, fields, models

IGNORED_MODELS = [
    'sale.order', 'purchase.order', 'crm.lead', 'project.project', 'project.task', 'account.invoice'
]


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _message_subscribe(self, partner_ids=None, channel_ids=None, subtype_ids=None, customer_ids=None):
        # Don't add partners as a followers for next models:
        if (self._name in IGNORED_MODELS) and partner_ids:
            users = self.env['res.users'].search([('partner_id', 'in', partner_ids)])
            # Only add contact as a follower if it has an assigned Odoo user
            partner_ids = users.mapped('partner_id').ids if users else []
        # Call to super with modified 'partner_ids' list
        return super(MailThread, self)._message_subscribe(
            partner_ids=partner_ids, channel_ids=channel_ids, subtype_ids=subtype_ids, customer_ids=customer_ids)
