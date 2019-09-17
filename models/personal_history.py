from odoo import fields, models, api


class PersonalHistory(models.Model):
    _name = 'personal.history'
    _description = "List of personal histories by the patients"

    name = fields.Char("Name")
    partner_ids = fields.Many2many("res.partner", 'personal_history_rel', 'personal_history_id', 'partner_id',
                                   string="Partners")

