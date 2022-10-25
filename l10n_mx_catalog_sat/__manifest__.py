# -*- coding: utf-8 -*-
# Copyright (C) 2022 GECOERP (http://www.gecoerp.com/)
# @author: Manuel Cabañas <manuel.cabanas@gecoerp.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Catálogos para Facturación Electrónica CFDI 4.0 (Mexico)',
    'description': ''' Catálogos para Factura Electrónica CFDI 4.0 (Mexico)
    ''',
    'category': 'Localisation',
    'license': 'OPL-1',  
    'author': 'Manuel Cabañas, GECOERP',
    'website': 'https://www.gecoerp.com',  
    'version': '16.01',
    'maintainers': ["gecoerp"],  
    'depends': [
        'sale','account','purchase'
    ],
    'data': [  
    ],
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'application': False,
    'installable': True,
}
