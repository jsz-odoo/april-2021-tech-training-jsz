# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ArtWork(models.Model):
    _name = 'art.work'
    _description = 'Art Work'
        
    nombre = fields.Char(string='Nombre', required=True)
    largo = fields.Float(string='Largo', default=1.0)
    anchura = fields.Float(string='Anchura', default=1.0)
    solo_admin = fields.Boolean(string='Opción para Administradores', groups="base.group_system")
    foto_obra = fields.Image(string='Fotografía de la Obra')
    