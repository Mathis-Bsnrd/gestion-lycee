from odoo import fields, models, api

class IutItModel(models.Model):
    _name = 'iut.course'
    
    name = fields.Char('Nom', required=True)
    