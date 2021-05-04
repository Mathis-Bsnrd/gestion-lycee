from odoo import fields, models, api

class IutItModel(models.Model):
    _name = 'iut.course'
    
    name = fields.Char('Nom', required=True)
    schedule_id = fields.Many2many('iut.schedule')