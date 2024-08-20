from odoo import models,fields,api,_
class DriversInformation(models.Model):
    _name = 'drivers.information'
    name = fields.Char('Driver name')
    national_id_card = fields.Char('National ID Card')
    driving_lis = fields.Char('Driving License')
    phone_num = fields.Char('Phone Number')
    national_expiry = fields.Date('National ID Expiration date')
    driving_expiry = fields.Date('Driving license  Expiration date')
