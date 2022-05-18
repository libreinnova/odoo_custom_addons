from odoo import _, api, fields, models


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _message_auto_subscribe_followers(self, updated_values, default_subtype_ids):
        subscribe_message = super(MailThread, self)._message_auto_subscribe_followers(
            updated_values, default_subtype_ids)
        # Return new message list without assigned notification entries
        return [
            value for value in subscribe_message if (len(value) > 2 and value[2] != 'mail.message_user_assigned')
        ]
