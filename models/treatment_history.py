from odoo import fields, models, api


class TreatmentHistory(models.Model):
    _name = 'treatment.history'
    _inherit = ['physiotherapy.fields']
    _description = "Each of sessions of a treatment"

    active = fields.Boolean(default=True)
    name = fields.Char("Name", required=True)
    treatment_id = fields.Many2one("partner.treatment", "Treatment")

    # CERVICAL
    cervical = fields.Boolean(related="treatment_id.cervical")
    cervical_act_over_ids = fields.One2many('treatment.movements', 'cervical_act_over_ids', "Cervical Act/Over")
    # - differentiation test
    cervical_dif_test_ids = fields.One2many('treatment.movements', 'cervical_dif_test_ids', "Differentiation Test")
    # - quadrants
    cervical_quadrant_ids = fields.One2many('treatment.movements', 'cervical_quadrant_ids', "Quadrant")
    # - PA movements
    cervical_pa_ids = fields.One2many('treatment.movements', 'cervical_pa_ids', "Cervical PA")
    # - physiological pasive movements
    cervical_physiological_passive_ids = fields.One2many('treatment.movements', 'cervical_physiological_passive_ids',
                                                         "Physiological Passive")
    # - special tests
    cervical_special_test_ids = fields.One2many('treatment.movements', 'cervical_special_test_ids', "Special Test")
    # - cervical evaluation
    cervical_evaluation_ids = fields.One2many('treatment.movements', 'cervical_evaluation_ids', "Cervical Evaluation")

    # DORSAL
    dorsal = fields.Boolean(related="treatment_id.dorsal")
    dorsal_act_over_ids = fields.One2many('treatment.movements', 'dorsal_act_over_ids', "Dorsal Act/Over")
    # - physiological pasive movements
    dorsal_physiological_passive_ids = fields.One2many('treatment.movements', 'dorsal_physiological_passive_ids',
                                                       "Physiological Passive")
    # - special tests
    dorsal_special_test_ids = fields.One2many('treatment.movements', 'dorsal_special_test_ids', "Special Test")
    # - PA movements
    dorsal_pa_ids = fields.One2many('treatment.movements', 'dorsal_pa_ids', "Cervical PA")
    # - thoracic assessment and costal displacement during breathing
    dorsal_thora_cost_ids = fields.One2many('treatment.movements', 'dorsal_thora_cost_ids',
                                            "Thoracic and costal evaluation")
    # - ribs evaluation PA
    dorsal_ribs_pa_ids = fields.One2many('treatment.movements', 'dorsal_ribs_pa_ids', "Ribs evaluation")
    # - diaphragm evaluation PG
    dorsal_diaphragm_ids = fields.One2many('treatment.movements', 'dorsal_diaphragm_ids', "Diaphragm evaluation PG")

    # LUMBAR
    lumbar = fields.Boolean(related="treatment_id.lumbar")
    lumbar_act_over_ids = fields.One2many('treatment.movements', 'lumbar_act_over_ids', "Lumbar Act/Over")
    # - accessory movement PA
    lumbar_accessory_ids = fields.One2many('treatment.movements', 'lumbar_accessory_ids', "Accessory movement PA")
    # - muscle evaluation lumbar and hip
    lumbar_hip_muscle_ids = fields.One2many('treatment.movements', 'lumbar_hip_muscle_ids',
                                            "Lumbar and hip muscle evaluation")
    # - mckenzie test
    lumbar_mckenzie_test_ids = fields.One2many('treatment.movements', 'lumbar_mckenzie_test_ids', "Mckenzie Test")
    # - sacroiliac tests
    lumbar_sacroiliac_test_ids = fields.One2many('treatment.movements', 'lumbar_sacroiliac_test_ids', "Sacroiliac Test")

    # SUPERIOR MEMBER
    superior = fields.Boolean(related="treatment_id.superior")
    superior_member_ids = fields.One2many('treatment.movements', 'superior_member_ids', "Sacroiliac Test")

    # INFERIOR MEMBER
    inferior = fields.Boolean(related="treatment_id.inferior")
    inferior_member_ids = fields.One2many('treatment.movements', 'inferior_member_ids', "Sacroiliac Test")

    # TEMPOROMANDIBULAR JOINT
    temporomandibular = fields.Boolean(related="treatment_id.temporomandibular")
    temporomandibular_joint_ids = fields.One2many('treatment.movements', 'temporomandibular_joint_ids',
                                                  "Temporomandibular Joint")

    @api.onchange('treatment_id')
    def _onchange_treatment_id(self):
        if self.treatment_id:
            self.partner_id = self.treatment_id.partner_id


