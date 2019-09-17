from odoo import fields, models, api
import pdb

FIELDS_PHYSIOTHERAPY = ['birth_date',
                        'gender',
                        'civil_state',
                        'allergies',
                        'style_of_life',
                        'sport_practice',
                        'sport_id',
                        'sport_periodicity',
                        'personal_history_id',
                        'familiar_history_id', ]


class ResPartner(models.Model):
    _inherit = 'res.partner'

    physiotherapy_partner = fields.Boolean("Physiotherapy Partner")
    birth_date = fields.Date('Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    civil_state = fields.Selection([('single', 'Single'), ('married', 'Married')], string="Civil State")
    allergies = fields.Char("Allergies")
    style_of_life = fields.Char("Style of life")
    sport_practice = fields.Boolean("Practice Sports??")
    sport_id = fields.Many2one("partner.sport", "Sport practice")
    sport_periodicity = fields.Selection([('two', '1 - 2 per week'),
                                          ('five', '2 - 5 per week'),
                                          ('seven', '6 or more')], string="Periodicity")
    personal_history_id = fields.Many2many("personal.history",  'personal_history_rel', 'partner_id',
                                           'personal_history_id', string="Personal history")
    familiar_history_id = fields.Many2many("familiar.history",  'familiar_history_rel', 'partner_id',
                                           'familiar_history_id', string="Familiar history")

    @api.model
    def create(self, values):
        self.check_physiotherapy(values)
        return super().create(values)

    @api.multi
    def write(self, values):
        self.check_physiotherapy(values)
        return super().write(values)

    @staticmethod
    def check_physiotherapy(values):
        """
        Method to mark what partners are physiotherapy patients also.
        """
        s1 = set(values.keys())
        s2 = set(FIELDS_PHYSIOTHERAPY)
        res = s1.intersection(s2)
        if res:
            values['physiotherapy_partner'] = True
