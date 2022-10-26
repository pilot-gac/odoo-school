from odoo import models, fields


class DiagnosisModel(models.Model):
    _name = 'diagnosis.model'
    _description = 'Diagnosis'

    name = fields.Char()

    patient_ids = fields.Many2one(
        comodel_name='patient.model')
