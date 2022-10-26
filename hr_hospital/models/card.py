from odoo import models, fields


class CardModel(models.Model):
    _name = 'card.model'
    _description = 'Card'

    name = fields.Char()

    Doctor = fields.Many2many(
        comodel_name='doctor.model'
    )
    Diagnosis = fields.Many2many(
        comodel_name='diagnosis.model'
    )
