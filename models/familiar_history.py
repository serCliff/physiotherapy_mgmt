from odoo import fields, models, api


class FamiliarHistory(models.Model):
    _name = 'familiar.history'
    _description = "List of familiar histories by the patients"

    name = fields.Char("Name")
    partner_ids = fields.Many2many("res.partner", 'familiar_history_rel', 'familiar_history_id', 'partner_id',
                                   string="Partners")

