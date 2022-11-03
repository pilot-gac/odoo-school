import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class PatientModel(models.Model):
    _name = 'patient.model'
    _description = 'Patient'

    surname = fields.Char(string='Прізвище', required=True, help='Обов\'язково')
    name = fields.Char(string='Ім\'я', required=True, help='Обов\'язково')
    patronymic = fields.Char(string='Ім\'я по батькові')
    gender = fields.Selection([('чоловіча', 'Чоловіча'), ('жіноча', 'Жіноча')], string="Стать", default='чоловіча')
    # gender = fields.Selection(selection='a_function_name')
    year_of_birth = fields.Date(string='Дата народження', default=fields.Date.context_today)
    age = fields.Integer(string='Вік')
    passport = fields.Char(string='Паспортні дані')
    contact_person = fields.Char(string='Контактна особа')

    active = fields.Boolean(
        default=True, )
    card = fields.Char(required=True)
    diagnosis = fields.Char()

    doctor_ids = fields.Many2many(
        comodel_name='doctor.model', )
    diagnosis_ids = fields.Many2many(
        comodel_name='diagnosis.model'
    )
