from odoo import fields, models, api, _
import pdb


class PartnerTreatment(models.Model):
    _name = 'partner.treatment'
    _inherit = ['physiotherapy.fields']
    _description = "Historical of some illness treatment. A treatment have some treatment.history"

    _sql_constraints = [
        ('intensity_now',
         'check(intensity_now >= 0 and intensity_now <= 10)',
         'The intensity should be between 0% and 10!'),
        ('intensity_most',
         'check(intensity_most >= 0 and intensity_most <= 10)',
         'The intensity when it hurst the most should be between 0% and 10!'),
    ]

    active = fields.Boolean(default=True)

    name = fields.Char("Name", required=True)
    observations = fields.Text("Observations", help="Duration? Origins? Influences?")

    treatment_history_ids = fields.One2many("treatment.history", "treatment_id", "Treatment Histories")
    history_count = fields.Integer(compute='count_history')

    # RED FLAGS
    several_illness = fields.Boolean()
    several_illness_text = fields.Char()
    movement_illness = fields.Boolean(help="Not modified with medication or postion")
    movement_illness_text = fields.Char()
    nocturnal_illness = fields.Boolean()
    nocturnal_illness_text = fields.Char()
    illness_without_background = fields.Boolean(help="Several illness without traumatic background")
    illness_without_background_text = fields.Char()
    several_muscle_spasm = fields.Boolean()
    several_muscle_spasm_text = fields.Char()
    psychological_trastorn = fields.Boolean()
    psychological_trastorn_text = fields.Char()
    missing_correlation = fields.Boolean(help="Missing correlation between test and physical researching")
    missing_correlation_text = fields.Char()
    hormonal_alterations = fields.Boolean()
    hormonal_alterations_text = fields.Char()

    # TYPE OF ILLNESS
    # - pathology
    neurophatic = fields.Boolean()
    nociceptive = fields.Boolean()
    psychogenic = fields.Boolean()
    # - course
    continuous = fields.Boolean()
    irruptive = fields.Boolean()
    incidental = fields.Boolean()
    # - location
    somatic = fields.Boolean()
    visceral = fields.Boolean()
    # - intensity
    intensity = fields.Selection([('mild', 'mild'), ('moderate', 'moderate'), ('severe', 'severe')])
    mechanic = fields.Boolean(help="Movement")
    mechanic_text = fields.Char()
    ischemic = fields.Boolean(help="About the day")
    ischemic_text = fields.Char()
    chemical_inflammatory = fields.Boolean("Chemical/Inflammatory", help="Night and rigidity")
    chemical_inflammatory_text = fields.Char()

    # LOCATION OF ILLNESS
    # - profundity
    shallow = fields.Boolean()
    deep = fields.Boolean()
    # - intensity
    intensity_now = fields.Integer()
    intensity_most = fields.Integer(help="Intensity when it hurst the most")
    # - irritating
    irritating_week = fields.Boolean(help="Irritating during the Week")
    irritating_week_text = fields.Char()
    irritating_weekend = fields.Boolean(help="Irritating during the Weekend")
    irritating_weekend_text = fields.Char()
    # - abnormal sensations
    abnormal_sensations = fields.Char()

    # BEHAVIOR OF SYMPTOMS
    # - limitations during the last 24 hours
    functionality = fields.Char(help="Functionality Limitations")
    positional = fields.Char(help="Rest, activity, positions held")
    pain_development = fields.Char(help="Pain development")
    # - aggravating
    aggravating = fields.Char()
    # - mitigating
    mitigating = fields.Char()
    # - diary activities
    diary_activities = fields.Char()

    # SPECIAL QUESTIONS
    dx_test = fields.Text()
    general_health = fields.Text()
    involuntary_thinning = fields.Boolean()
    social_history = fields.Text()
    medicines = fields.Text()
    emotional_factors = fields.Text()
    hormonal_factors = fields.Text()
    headache = fields.Text(help="Dizziness, headache, painful trivial activity")
    treatments_received = fields.Text()

    # HISTORY
    what_happens = fields.Text()
    environment = fields.Text(help="When? How? Where?")

    # HYPOTHESIS
    initial_hypothesis = fields.Text(required=True)

    # TREATMENT HISTORY
    cervical = fields.Boolean(default=lambda self: self._default_values('cervical'))
    dorsal = fields.Boolean(default=lambda self: self._default_values('dorsal'))
    lumbar = fields.Boolean(default=lambda self: self._default_values('lumbar'))
    superior = fields.Boolean(default=lambda self: self._default_values('superior'))
    inferior = fields.Boolean(default=lambda self: self._default_values('inferior'))
    temporomandibular = fields.Boolean(default=lambda self: self._default_values('temporomandibular'))

    @api.multi
    def count_history(self):
        if self.treatment_history_ids:
            self.history_count = len(self.treatment_history_ids.ids)

    @api.multi
    def action_make_session(self):
        action = self.env.ref('physiotherapy_mgmt.action_treatment_history_form').read()[0]
        action['context'] = {'search_default_treatment_id': self.id}
        if len(self.treatment_history_ids) == 1:
            action['res_id'] = self.treatment_history_ids.id
            action['target'] = 'current'
            action['view_mode'] = 'form'
            del action['views']
        return action
