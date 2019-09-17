from odoo import fields, models, api


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

