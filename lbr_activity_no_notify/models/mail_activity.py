# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class MailActivity(models.Model):
    _inherit = 'mail.activity'

    @api.multi
    def action_notify(self):
        return True
