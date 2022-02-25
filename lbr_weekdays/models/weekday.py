# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class Weekday(models.Model):
    _name = 'weekday.weekday'
    _description = 'Weekday'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence', default=10)
    name = fields.Char('Name', required=True, translate=True)
    code = fields.Char('Code', required=True)
    weekend = fields.Boolean('Is weekend')

    _sql_constraints = [
        ('weekday_weekday_name_unique', 'unique (name)', 'The weekday name must be unique!'),
        ('weekday_weekday_code_unique', 'unique (code)', 'The weekday code must be unique!')
    ]
