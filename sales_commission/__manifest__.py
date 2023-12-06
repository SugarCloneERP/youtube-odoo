# -*- coding: utf-8 -*-

{
    'name': 'Sales Commission',
    'version': '17.0.1.0',
    'summary': 'Sales Person Commission',
    'sequence': 10,
    'category': 'CRM/Sales',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_commission_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'AGPL-3'
}
