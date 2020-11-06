# -*- coding: utf-8 -*-
{
    'name': "Products API",
    'author': 'Vipul Patel',
    'summary': """
        Products api module help to get information of product base on requested product id.
    """,
    'description': "",
    'category': 'Tools/API',
    'version': '13.0.0.1',
    'depends': [
        'stock',
    ],
    'external_dependencies': {
    },
    'data': [
        'data/user_data.xml',
        'views/users_view.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
