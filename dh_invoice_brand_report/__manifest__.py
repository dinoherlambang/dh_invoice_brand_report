# -*- coding: utf-8 -*-
{
    'name': "dh_invoice_brand_report",

    'summary': """
        Add product_brand in invoice print out""",

    'description': """
        This module enhances invoice reports by adding product brand information to the PDF printouts.
        Key features include:
        - Adds a 'Brand' column to invoice report PDFs
        - Integrates seamlessly with existing Odoo invoice templates
        - Improves clarity and professionalism in your billing process
        - Easy to install and configure
        - Compatible with Odoo 13.0
        
        This module is designed to provide more detailed and brand-specific information on customer invoices,
        helping businesses to better showcase their product offerings and improve customer communication.
    """,

    'author': "dinoherlambang",
    'website': "http://instagram.com/_dinoherlambang_/",

    'category': 'Accounting',
    'version': '13.0',
    # ... other manifest data ...
    'depends': ['base', 'account', 'product', 'product_brand'],
    'external_dependencies': {
        'python': [],
        'bin': [],
        'git': ['https://github.com/OCA/brand 13.0'],
    },

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
