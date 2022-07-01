{
    "name": "Stakeholder management",
    "summary": 'Manage stakeholder',
    "version": "2.0",
    "author": "Younes Yahia && Nasri Mohammed",
    "website": "http://www.eficent.com",
    "category": "Generic Modules/Projects & Services",
    "depends": [
        "base",
        "project",
    ],
    "description": """ This module offers the possibility to register at project level the stakeholders involved in a project.
        - It adds a 'Stakeholders' tab in the project form.
        - The stakeholder can be registered as a partner, or a contact person. 
        - You can specify the roles and responsibilities of the stakeholders in this project.
        - You can maintain a master data for roles and responsibilities.
    """,
    "init_xml": [
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/project_security.xml",
        "project_hr_role.xml",
        "project_hr_task.xml",
        "project_hr_stakeholder.xml",
        # "project_hr_stakeholder_data.xml",
    ],
    'demo_xml': [

    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'active': False,
    'certificate': '',

}
