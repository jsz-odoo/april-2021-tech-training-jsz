# -*- coding: utf-8 -*-

{
    "name": 'Art Gallery',
    
    "summary": """
        An app to manage art pieces for the Gallery.
    """,
    
    "description": """
        An art gallery management app with the following features:
        - Create, edit, delete art pieces.
        - View art piece details.
    """,
    
    "author": "Johnny Sanchez",
    
    "category": "Custom Development",
    
    "version": "0.1",
    
    "depends": ["base", "contacts", "stock", "website"],
    
    "data": [
        "security/art_gallery_security.xml",
        "security/ir.model.access.csv",
        "views/art_gallery_views.xml",
        "views/art_gallery_menuitems.xml",
        "views/product_template_views.xml",
        "views/gallery_web_templates.xml",
        "data/art_gallery_data.xml",
    ],
    
    "demo": [
        "demo/demo.xml"
    ],
    
    "license": "OEEL-1",
}