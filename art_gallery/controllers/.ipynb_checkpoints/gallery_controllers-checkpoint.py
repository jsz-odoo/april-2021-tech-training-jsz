# -*- coding: utf-8 -*-
from odoo import http


class Gallery(http.Controller):
    @http.route('/gallery/', auth='public', website='True')
    def index(self, **kw):
        return 'Hello, world'
    
    @http.route('/gallery/art/', auth='public', website=True)
    def courses(self, **kw):
        art = http.request.env['art.work'].search([])
        return http.request.render('art_gallery.gallery_site', {
            'art': art,
        })