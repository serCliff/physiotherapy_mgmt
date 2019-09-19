from odoo import fields, models, api


class TreatmentHistory(models.Model):
    _name = 'treatment.history'
    _inherit = ['physiotherapy.fields']
    _description = "Each of histories of a treatment"

    active = fields.Boolean(default=True)
    name = fields.Char("Name", required=True)
    treatment_id = fields.Many2one("partner.treatment", "Treatment")

    # CERVICAL
    cervical = fields.Boolean(default=False)
    cervical_act_over_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Cervical Act/Over")
    # - differentiation test
    cervical_dif_test_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Differentiation Test")
    # - quadrants
    cervical_quadrant_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Quadrant")
    # - PA movements
    cervical_pa_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Cervical PA")
    # - physiological pasive movements
    cervical_physiological_passive_ids = fields.One2many('treatment.movements', 'treatment_history_id',
                                                         "Physiological Passive")
    # - special tests
    cervical_special_test_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Special Test")
    # - cervical evaluation
    cervical_evaluation_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Cervical Evaluation")

    # DORSAL
    dorsal = fields.Boolean(default=False)
    dorsal_act_over_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Dorsal Act/Over")
    # - physiological pasive movements
    dorsal_physiological_passive_ids = fields.One2many('treatment.movements', 'treatment_history_id',
                                                       "Physiological Passive")
    # - special tests
    dorsal_special_test_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Special Test")
    # - PA movements
    dorsal_pa_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Cervical PA")
    # - thoracic assessment and costal displacement during breathing
    dorsal_thora_cost_ids = fields.One2many('treatment.movements', 'treatment_history_id',
                                            "Thoracic and costal evaluation")
    # - ribs evaluation PA
    dorsal_ribs_pa_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Ribs evaluation")
    # - diaphragm evaluation PG
    dorsal_diaphragm_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Diaphragm evaluation PG")

    # LUMBAR
    lumbar = fields.Boolean(default=False)
    lumbar_act_over_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Lumbar Act/Over")
    # - accessory movement PA
    lumbar_accessory_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Accessory movement PA")
    # - muscle evaluation lumbar and hip
    lumbar_hip_muscle_ids = fields.One2many('treatment.movements', 'treatment_history_id',
                                            "Lumbar and hip muscle evaluation")
    # - mckenzie test
    lumbar_mckenzie_test_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Mckenzie Test")
    # - sacroiliac tests
    lumbar_sacroiliac_test_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Sacroiliac Test")

    # SUPERIOR MEMBER
    superior = fields.Boolean(default=False)
    superior_member_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Sacroiliac Test")

    # INFERIOR MEMBER
    inferior = fields.Boolean(default=False)
    inferior_member_ids = fields.One2many('treatment.movements', 'treatment_history_id', "Sacroiliac Test")

    # TEMPOROMANDIBULAR JOINT
    temporomandibular = fields.Boolean(default=False)
    temporomandibular_joint_ids = fields.One2many('treatment.movements', 'treatment_history_id',
                                                  "Temporomandibular Joint")

