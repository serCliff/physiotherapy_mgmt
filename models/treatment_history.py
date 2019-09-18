from odoo import fields, models, api


class TreatmentHistory(models.Model):
    _name = 'treatment.history'
    _inherit = ['physiotherapy.fields']
    _description = "Each of histories of a treatment"

    name = fields.Char("Name")
    treatment_id = fields.Many2one("partner.treatment", "Treatment")


