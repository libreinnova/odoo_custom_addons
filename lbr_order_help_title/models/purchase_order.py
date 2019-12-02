from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    help_title = fields.Char('Help title', help='Additional order help title')
