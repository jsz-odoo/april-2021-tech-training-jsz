# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    art_work_id = fields.Many2one(string='Art Piece', comodel_name='art.work')
    is_art_work = fields.Boolean(string='Is Art Piece')
