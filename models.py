# -*- coding: utf-8 -*-
import string
from odoo import models, fields, tools, api
# from odoo.tools.translate import _


class Project_hr_task(models.Model):
    _name = "project.hr.task"
    _description = 'Project action'

    name = fields.Char(string='Action', size=128, required=True, translate=True)
    description = fields.Text('Description', translate=True)


class Project_hr_role(models.Model):
    _name = "project.hr.role"
    _description = "Project Role"

    code = fields.Char(string="Code", required=True)
    name = fields.Char(string="Name", size=128, required=True, translate=True)
    description = fields.Text(string="Description", translate=True)


class Project_hr_stakeholder(models.Model):
    _name = "project.hr.stakeholder"
    _description = 'Project Stakeholder'

    id = fields.Char(string="ID", required=True, size=64)

    # type = fields.Char(string="Type", required=True, size=64)
  
    type = fields.Selection([
        ('Interne', 'Interne'),
        ('Externe', 'Externe')
    ], string='Type', default='Interne')

    strategy = fields.Selection([
        ('Acteur Cle', 'Acteur Cle'),
        ('Garder Informe', 'Garder Informe'),
        ('Effort Minimale', 'Effort Minimale'),
        ('Garderr Satisfait', 'Garderr Satisfait')
    ], string='Strategie', default='Acteur Cle')

    role_ids = fields.Many2many('project.hr.role', 'stakeholder_role_rel', 'stakeholder_id', 'role_id', 'Roles',
                                help='The assignment of the roles and responsibilities determines what actions the project manager,' \
                                     'project team member,or individual contributor will have in the project. Roles and responsibilities' \
                                     ' generally support the project scope since this is the required work for the project.')

    partner_id = fields.Many2one('res.partner', 'Contact', required=True)
    # contact = fields.Many2one('res.partner.email', 'Email', required=True)

    contribution = fields.Char(string="Contribution", required=True, size=64)
    attentes = fields.Char(string="Attentes", required=True, size=64)
    project_id = fields.Many2one('project.project', 'Project', ondelete='cascade')
    email = fields.Char('Email', related='partner_id.email')

    """namse = fields.Char(related="res.partner.name", string="Store Name", store=True, invisible="1")"""

    interet = fields.Selection([
        ('Faible', 'Faible'),
        ('Eleve', 'Eleve')
    ], string='Interet', required=True)

    pouvoir = fields.Selection([
        ('Faible', 'Faible'),
        ('Eleve', 'Eleve')
    ], string='Pouvoir', required=True)


    action_ids = fields.Many2many('project.hr.task', 'stakeholder_action_rel', 'stakeholder_id', 'action_id',
                                  'Actions',
                                  help='The assignment of the roles and responsibilities determines what actions the project manager,' \
                                       'project team member,or individual contributor will have in the project. Roles and responsibilities' \
                                       ' generally support the project scope since this is the required work for the project.')


class Project(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    stakeholder_ids = fields.One2many('project.hr.stakeholder', 'project_id', 'Stakeholders'),

# project()
