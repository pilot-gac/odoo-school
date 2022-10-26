import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class PatientModel(models.Model):
    _name = 'patient.model'
    _description = 'Patient'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
    card = fields.Char()
    diagnosis = fields.Char()

    doctor_ids = fields.Many2many(
        comodel_name='doctor.model', )
    diagnosis_ids = fields.Many2many(
        comodel_name='diagnosis.model'
    )
