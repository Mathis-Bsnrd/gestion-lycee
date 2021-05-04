from odoo import fields, models, api

class IutModelType(models.Model):
    _name = 'iut.schedule'
    
    date_start = fields.Datetime('Horaire Début', required = True)
    date_stop = fields.Datetime('Horaire Fin', required = True)
    room = fields.Char('Salle de classe', required = True)
    class_id = fields.Many2many('iut.class')
    course_id = fields.Many2many('iut.course')