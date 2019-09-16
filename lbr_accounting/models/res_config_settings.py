from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_om_account_accountant = fields.Boolean(
        string="Odoo12 Accounting (by Odoo Mates & Odoo SA)",
        help="Accounting Reports, Asset Management and Account Budget For Odoo12 Community Edition")
