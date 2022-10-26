import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class DoctorModel(models.Model):
    _name = 'doctor.model'
    _description = 'Doctor'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
