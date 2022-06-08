# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Payroll',
    'category': 'Human Resources',
    'summary': 'Manage your employee payroll records',
    'version': '15.0.1.0.0',
    'sequence': 1,
    "license": "LGPL-3",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    'website': 'http://www.serpentcs.com',
    'description': "",
    'depends': [
        'hr_contract',
        'hr_holidays',
        'base',
    ],
    'data': [
        'security/hr_payroll_security.xml',
        'security/ir.model.access.csv',
        'wizard/hr_payroll_payslips_by_employees_views.xml',
        'views/hr_contract_views.xml',
        'views/hr_salary_rule_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_employee_views.xml',
        'data/hr_payroll_sequence.xml',
        'views/hr_payroll_report.xml',
        'data/hr_payroll_data.xml',
        'wizard/hr_payroll_contribution_register_report_views.xml',
        'views/res_config_settings_views.xml',
        'views/report_contributionregister_templates.xml',
        'views/report_payslip_templates.xml',
        'views/report_payslipdetails_templates.xml',
    ],

    "installable": True,
    "auto_install": False,
    'price': 35,
    'currency': 'EUR',
}
