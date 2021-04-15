# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ArtWork(models.Model):
    _name = 'art.work'
    _description = 'Art Work'
    _rec_name = 'nombre'
        
    nombre = fields.Char(string='Nombre', required=True)
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
    precio = fields.Float(string="Precio", required=True)
    en_venta = fields.Boolean(string="En Venta")
    
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