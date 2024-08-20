from odoo import models,fields,api,_
class BusInformation(models.Model):
    _name = 'bus.information'
    name = fields.Char('Bus number')
    bus_name= fields.Char('Bus name')
    bus_type = fields.Selection([
        ('hi As', 'High As'),
        ('coaster', 'Coaster'),
        ('chevorlet', 'Chevorlet'),
    ],string='Bus Model')
    bus_matron = fields.Many2one('hr.employee', 'Matron name')
    number_of_seats = fields.Integer('Number of seats')
    bus_faceplate= fields.Char('Bus facepalte')
    bus_route = fields.Text('Bus route')
    bus_contact88 = fields.One2many('res.partner', 'bus_number_notion',string='Bus')
    bus_employee_view = fields.One2many('hr.employee', 'bus_employee', string='Staff members')
class ResPartnerNotion(models.Model):
    _inherit = 'res.partner'
    bus_number_notion = fields.Many2one('bus.information', string='Bus Number')
    bus_parent_phone = fields.Char('Parent/Bus contact number')


class HrEmployeeEdit(models.Model):
    _inherit = 'hr.employee'
    bus_service = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ])
    bus_employee = fields.Many2one('bus.information', string= 'Bus Number')
    bus_address = fields.Text('Bus address')
    bus_contact_phone = fields.Char('Parent/Bus contact number')




