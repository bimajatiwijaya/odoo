# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Claims Management',
    'version': '1.0',
    'category': 'Sales',
    'description': """

Manage Customer Claims.
=======================
This application allows you to track your customers/vendors claims and grievances.

It is fully integrated with the email gateway so that you can create
automatically new claims based on incoming emails.
    """,
    'depends': ['crm'],
    'data': [
        'data/crm_claim_data.xml',
        'security/ir.model.access.csv',
        'views/crm_claim_view.xml',
        'views/crm_claim_menu.xml',
        'views/res_partner_view.xml',
        'report/crm_claim_report_view.xml',
    ],
    'demo': ['data/crm_claim_demo.xml'],
    'test': [
        'test/process/claim.yml',
        'test/ui/claim_demo.yml'
    ],
    'installable': True,
    'auto_install': False,
}
