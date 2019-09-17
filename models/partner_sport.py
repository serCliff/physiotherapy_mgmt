from odoo import fields, models, api


class PartnerSport(models.Model):
    _name = 'partner.sport'
    _description = "List of sports which are practiced by the patients"

    name = fields.Char("Name")
    partner_ids = fields.One2many("res.partner", "sport_id", "Partners")

