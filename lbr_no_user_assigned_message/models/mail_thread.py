from odoo import _, api, fields, models


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _message_auto_subscribe_followers(self, updated_values, default_subtype_ids):
        message = super(MailThread, self)._message_auto_subscribe_followers(updated_values, default_subtype_ids)
        new_message = []
        for values in message:
            if len(values) == 3:
                if values[2] == 'mail.message_user_assigned':
                    continue
            else:
                new_message.append(values)
        # Return new message list without assigned notification entries
        return new_message
