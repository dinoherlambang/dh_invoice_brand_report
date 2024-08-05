# -*- coding: utf-8 -*-
{
    'name': "dh_invoice_brand_report",

    'summary': """
        Add product_brand in invoice print out""",

    'description': """
        
    """,

    'author': "My Company",
    'website': "http://instagram.com/_dinoherlambang_/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account','product','product_brand'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/report_invoice_document.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
