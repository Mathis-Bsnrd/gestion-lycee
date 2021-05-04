from odoo import fields, models, api

class IutItDevice(models.Model):
    _name = 'iut.student'
    
    firstname = fields.Char('Prénom', required=True)
    lastname = fields.Char('Nom', required=True)
    birthdate = fields.Date('Date de naissance', required=True)
    age = fields.Integer('Age', required=True)
    class_id = fields.Many2one('iut.class')