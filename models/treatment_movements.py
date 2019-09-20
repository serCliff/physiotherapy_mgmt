from odoo import fields, models, api


class TreatmentMovements(models.Model):
    _name = 'treatment.movements'
    _description = "List of movements"

    sequence = fields.Integer()
    name = fields.Char(required=True)
    type1_right = fields.Char()
    type1_left = fields.Char()
    type2_right = fields.Char()
    type2_left = fields.Char()
    type3_right = fields.Char()
    type3_left = fields.Char()
    central = fields.Char()

    cervical_act_over_ids = fields.Many2one('treatment.history')
    cervical_dif_test_ids = fields.Many2one('treatment.history')
    cervical_quadrant_ids = fields.Many2one('treatment.history')
    cervical_pa_ids = fields.Many2one('treatment.history')
    cervical_physiological_passive_ids = fields.Many2one('treatment.history')
    cervical_special_test_ids = fields.Many2one('treatment.history')
    cervical_evaluation_ids = fields.Many2one('treatment.history')
    dorsal_act_over_ids = fields.Many2one('treatment.history')
    dorsal_physiological_passive_ids = fields.Many2one('treatment.history')
    dorsal_special_test_ids = fields.Many2one('treatment.history')
    dorsal_pa_ids = fields.Many2one('treatment.history')
    dorsal_thora_cost_ids = fields.Many2one('treatment.history')
    dorsal_ribs_pa_ids = fields.Many2one('treatment.history')
    dorsal_diaphragm_ids = fields.Many2one('treatment.history')
    lumbar_act_over_ids = fields.Many2one('treatment.history')
    lumbar_accessory_ids = fields.Many2one('treatment.history')
    lumbar_hip_muscle_ids = fields.Many2one('treatment.history')
    lumbar_mckenzie_test_ids = fields.Many2one('treatment.history')
    lumbar_sacroiliac_test_ids = fields.Many2one('treatment.history')
    superior_member_ids = fields.Many2one('treatment.history')
    inferior_member_ids = fields.Many2one('treatment.history')
    temporomandibular_joint_ids = fields.Many2one('treatment.history')
