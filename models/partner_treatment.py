from odoo import fields, models, api, _


class PartnerTreatment(models.Model):
    _name = 'partner.treatment'
    _inherit = ['physiotherapy.fields']
    _description = "Historical of some illness treatment"

    _sql_constraints = [
        ('intensity_now',
         'check(intensity_now >= 0 and intensity_now <= 10)',
         'The intensity should be between 0% and 10!'),
        ('intensity_most',
         'check(intensity_most >= 0 and intensity_most <= 10)',
         'The intensity when it hurst the most should be between 0% and 10!'),
    ]

    name = fields.Char("Name", required=True)
    observations = fields.Text("Observations", help="Duration? Origins? Influences?")

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



