from odoo import fields, models, api

class res_partner(models.Model):
    class_ids = fields.Many2many('iut.class')
    inherit='res.partner'