# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class ArtWork(models.Model):
    _name = 'art.work'
    _description = 'Art Work'
    _rec_name = 'nombre'
    _inherit = ['mail.thread', 'mail.activity.mixin']
        
    nombre = fields.Char(string='Nombre', required=True, tracking=True)
    largo = fields.Float(string='Largo', default=1.0)
    anchura = fields.Float(string='Anchura', default=1.0)
    solo_admin = fields.Boolean(string='Opción para Administradores', groups="base.group_system")
    foto_obra = fields.Image(string='Fotografía de la Obra', max_width=800, max_height=600)
    state = fields.Selection(string="Estado", selection=[
        ('almacenado', 'Almacenado'),
        ('exhibicion', 'En exhibición'),
        ('vendido', 'Vendido')
    ], default='almacenado')
    peso = fields.Float(string="Peso", states={
        'almacenado': [('required', True)],
        'exhibicion': [('readonly', True)],
        'vendido': [('invisible', True)]
    })
    precio = fields.Float(string='Precio', required=True, group_operator="sum", tracking=True)
    en_venta = fields.Boolean(string="En Venta", tracking=True)
    artist_id = fields.Many2one(string='Artista', comodel_name='res.partner')
    display_date_start = fields.Date(string="Display Start")
    display_date_end = fields.Date(string="Display End")
    
    def almacenar(self):
        self.state = 'almacenado'
        
    def exhibir(self):
        self.state = 'exhibicion'
        
    def vender(self):
        self.state = 'vendido'

    def poner_en_venta(self):
        for obra in self:
            obra.en_venta = True
    
    def remover_de_venta(self):
        for obra in self:
            self.en_venta = False
            
    def ir_a_pagina(self):
        return {
            "type": "ir.actions.act_url",
            "url": "https://www.unam.mx/",
            "target": "new",
        }
    
    @api.constrains('largo')
    def _check_largo(self):
        for obra in self:
            if obra.largo <= 0:
                raise ValidationError('Largo debe tener un valor positivo.')
    
    @api.constrains('anchura')
    def _check_anchura(self):
        for obra in self:
            if obra.anchura <= 0:
                raise ValidationError('Anchura debe tener un valor positivo.')

    @api.constrains('display_date_end')
    def _check_display_date_end(self):
        for obra in self:
            if obra.display_date_end < obra.display_date_start:
                raise ValidationError('End date needs to be greater or equal to start date.')