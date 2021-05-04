# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : """{Lycée}""",
    'version' : '1.1',
    'summary': 'module gestion lycée',
    'category': 'Accounting/Accounting',

    'author': 'IT-Projects LLC, {}',
    'support': '',
    'website': '',
    'license': 'LGPL-3',

    'images' : [],
    'depends' : [],

    "external_dependencies": {"python": [], "bin": []},

    'data': [
        'views/iut_student_action.xml',
        'views/iut_class_action.xml',
        'views/iut_course_action.xml',
        'views/iut_schedule_action.xml',
        'views/res_partner_action.xml',
        'views/iut_lycee_menu.xml'

    ],
    'qweb': [
    ],
    'demo': [
    ],    

    'installable': True,
    'auto_install': False,
    'pre_init_hook': None,
    'post_init_hook': None,
    'post_onload': None,
}
