from odoo import fields, models, api


class BusMaintenance(models.Model):
    _name = 'bus.maintenance'
    type = fields.Selection([
        ('main', 'Maintenance'),
        ('fuel', 'Fuel'),
    ])
    amount_inv = fields.Integer('Invoice Amount')
    first_read = fields.Integer('First read')
    second_read = fields.Integer('Second read')
    result_read = fields.Integer('Total Kilometers', compute='total_kilo')
    name = fields.Char('Maintenance name')
    date = fields.Date('Date')
    upload = fields.Binary('Upload Invoice')
    notes = fields.Text('Description')
    bus_number = fields.Many2one('bus.information', 'Bus number')

    @api.depends('first_read', 'second_read')
    def total_kilo(self):
        for rec in self:
            if rec.type == 'fuel':
                rec.result_read = rec.second_read - rec.first_read
            else:
                rec.result_read == 0

