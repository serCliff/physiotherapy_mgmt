from odoo import fields, models, api


class TreatmentHistory(models.Model):
    _name = 'treatment.history'
    _inherit = ['physiotherapy.fields']
    _description = "Each of sessions of a treatment"

    name = fields.Char("Name", required=True)
    treatment_id = fields.Many2one("partner.treatment", "Treatment")

    # CERVICAL
    cervical = fields.Boolean(related="treatment_id.cervical")
    cervical_act_over_ids = fields.One2many('treatment.movements', 'cervical_act_over_ids', "Cervical Act/Over",
                                            default=lambda self: self._default_values('cervical_act_over_ids'))
    # - differentiation test
    cervical_dif_test_ids = fields.One2many('treatment.movements', 'cervical_dif_test_ids', "Differentiation Test",
                                            default=lambda self: self._default_values('cervical_dif_test_ids'))
    # - quadrants
    cervical_quadrant_ids = fields.One2many('treatment.movements', 'cervical_quadrant_ids', "Quadrant",
                                            default=lambda self: self._default_values('cervical_quadrant_ids'))
    # - PA movements
    cervical_pa_ids = fields.One2many('treatment.movements', 'cervical_pa_ids', "Cervical PA",
                                      default=lambda self: self._default_values('cervical_pa_ids'))
    # - physiological pasive movements
    cervical_physiological_passive_ids = fields.One2many('treatment.movements', 'cervical_physiological_passive_ids',
                                                         "Physiological Passive",
                                                         default=lambda self:
                                                         self._default_values('cervical_physiological_passive_ids'))
    # - special tests
    cervical_special_test_ids = fields.One2many('treatment.movements', 'cervical_special_test_ids', "Special Test",
                                                default=lambda self: self._default_values('cervical_special_test_ids'))
    # - cervical evaluation
    cervical_evaluation_ids = fields.One2many('treatment.movements', 'cervical_evaluation_ids', "Cervical Evaluation",
                                              default=lambda self: self._default_values('cervical_evaluation_ids'))

    # DORSAL
    dorsal = fields.Boolean(related="treatment_id.dorsal")
    dorsal_act_over_ids = fields.One2many('treatment.movements', 'dorsal_act_over_ids', "Dorsal Act/Over",
                                          default=lambda self: self._default_values('dorsal_act_over_ids'))
    # - physiological pasive movements
    dorsal_physiological_passive_ids = fields.One2many('treatment.movements', 'dorsal_physiological_passive_ids',
                                                       "Physiological Passive",
                                                       default=lambda self:
                                                       self._default_values('dorsal_physiological_passive_ids'))
    # - special tests
    dorsal_special_test_ids = fields.One2many('treatment.movements', 'dorsal_special_test_ids', "Special Test",
                                              default=lambda self: self._default_values('dorsal_special_test_ids'))
    # - PA movements
    dorsal_pa_ids = fields.One2many('treatment.movements', 'dorsal_pa_ids', "Cervical PA",
                                    default=lambda self: self._default_values('dorsal_pa_ids'))
    # - thoracic assessment and costal displacement during breathing
    dorsal_thora_cost_ids = fields.One2many('treatment.movements', 'dorsal_thora_cost_ids', "Thoracic and costal evaluation",
                                            default=lambda self: self._default_values('dorsal_thora_cost_ids'))
    # - ribs evaluation PA
    dorsal_ribs_pa_ids = fields.One2many('treatment.movements', 'dorsal_ribs_pa_ids', "Ribs evaluation",
                                         default=lambda self: self._default_values('dorsal_ribs_pa_ids'))
    # - diaphragm evaluation PG
    dorsal_diaphragm_ids = fields.One2many('treatment.movements', 'dorsal_diaphragm_ids', "Diaphragm evaluation PG",
                                           default=lambda self: self._default_values('dorsal_diaphragm_ids'))

    # LUMBAR
    lumbar = fields.Boolean(related="treatment_id.lumbar")
    lumbar_act_over_ids = fields.One2many('treatment.movements', 'lumbar_act_over_ids', "Lumbar Act/Over",
                                          default=lambda self: self._default_values('lumbar_act_over_ids'))
    # - accessory movement PA
    lumbar_accessory_ids = fields.One2many('treatment.movements', 'lumbar_accessory_ids', "Accessory movement PA",
                                           default=lambda self: self._default_values('lumbar_accessory_ids'))
    # - muscle evaluation lumbar and hip
    lumbar_hip_muscle_ids = fields.One2many('treatment.movements', 'lumbar_hip_muscle_ids',
                                            "Lumbar and hip muscle evaluation",
                                            default=lambda self: self._default_values('lumbar_hip_muscle_ids'))
    # - mckenzie test
    lumbar_mckenzie_test_ids = fields.One2many('treatment.movements', 'lumbar_mckenzie_test_ids', "Mckenzie Test",
                                               default=lambda self: self._default_values('lumbar_mckenzie_test_ids'))
    # - sacroiliac tests
    lumbar_sacroiliac_test_ids = fields.One2many('treatment.movements', 'lumbar_sacroiliac_test_ids', "Sacroiliac Test",
                                                 default=lambda self:
                                                 self._default_values('lumbar_sacroiliac_test_ids'))

    # SUPERIOR MEMBER
    superior = fields.Boolean(related="treatment_id.superior")
    superior_member_ids = fields.One2many('treatment.movements', 'superior_member_ids', "Sacroiliac Test",
                                          default=lambda self: self._default_values('superior_member_ids'))

    # INFERIOR MEMBER
    inferior = fields.Boolean(related="treatment_id.inferior")
    inferior_member_ids = fields.One2many('treatment.movements', 'inferior_member_ids', "Sacroiliac Test",
                                          default=lambda self: self._default_values('inferior_member_ids'))

    # TEMPOROMANDIBULAR JOINT
    temporomandibular = fields.Boolean(related="treatment_id.temporomandibular")
    temporomandibular_joint_ids = fields.One2many('treatment.movements', 'temporomandibular_joint_ids',
                                                  "Temporomandibular Joint",
                                                  default=lambda self:
                                                  self._default_values('temporomandibular_joint_ids'))

    @api.onchange('treatment_id')
    def _onchange_treatment_id(self):
        if self.treatment_id:
            self.partner_id = self.treatment_id.partner_id


