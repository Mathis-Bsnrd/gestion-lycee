from odoo import fields, models, api

class IutItBrand(models.Model):
    _name = 'iut.class'
    
    name = fields.Char('Nom', required = True)
    level = fields.Selection([('level1', 'Seconde'),('level2', 'Première'),('level3', 'Terminale')], 'level', default='level1')
    teacher_ids = fields.Many2many('iut.prof')
    student_ids = fields.Many2one('iut.student')
    student_nb = fields.Integer('Nombre d`élèves')
    