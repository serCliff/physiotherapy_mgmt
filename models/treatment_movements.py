from odoo import fields, models, api


class TreatmentMovements(models.Model):
    _name = 'treatment.movements'
    _description = "List of movements"

    treatment_history_id = fields.Many2one('treatment.history', "Treatment History")

    sequence = fields.Integer()
    name = fields.Char(required=True)
    type1_right = fields.Char()
    type1_left = fields.Char()
    type2_right = fields.Char()
    type2_left = fields.Char()
    type3_right = fields.Char()
    type3_left = fields.Char()
    central = fields.Char()


