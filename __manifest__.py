# -*- coding: utf-8 -*-
{
    'name': "Physioterapy Management",

    'summary': """
        Medical Clinic of Physioterapy Management
        """,

    'author': "Sergio Del Castillo",
    'website': "https://github.com/serCliff/",

    'category': 'medical',
    "contributors": [
        "Sergio Del Castillo <sergio.delcastillo@ecoitec.com>",
    ],
    'version': '0.1',

    'depends': [
        'sale',
    ],

    'data': [
        'data/treatment_data.xml',
        'security/physioterapy_security.xml',
        'security/ir.model.access.csv',
        'views/physiotherapy_view.xml',
        'views/res_partner.xml',
        'views/treatment_history.xml',
        'views/partner_treatment.xml',
    ],

}
