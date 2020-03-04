from odoo import fields, models


class Picking(models.Model):
    _inherit = "stock.picking"

    supplier_number = fields.Char(string="Supplier number")
    supplier_date = fields.Date(string="Supplier date")
