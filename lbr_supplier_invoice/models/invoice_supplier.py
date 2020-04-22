from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    supplier_number = fields.Char(string="Supplier number")
    supplier_date = fields.Date(string="Supplier date")
