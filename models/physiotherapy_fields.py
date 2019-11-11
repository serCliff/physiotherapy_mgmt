from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import pdb


class PartnerRelatedFields(models.AbstractModel):
    _name = "physiotherapy.fields"
    _description = "Fields related with partner to be used on physiotherapy"

    active = fields.Boolean(default=True)
    partner_id = fields.Many2one("res.partner", "Partner", required=True)
    create_date = fields.Datetime(default=lambda self: fields.Datetime.now())
    company_id = fields.Many2one('res.company', string='Company', index=True,
                                 default=lambda self: self.env.user.company_id.id)

    # Partner related fields
    birth_date = fields.Date(related='partner_id.birth_date')
    gender = fields.Selection(related='partner_id.gender')
    civil_state = fields.Selection(related='partner_id.civil_state')
    allergies = fields.Char(related='partner_id.allergies')
    function = fields.Char(related='partner_id.function')
    style_of_life = fields.Char(related='partner_id.style_of_life')
    sport_practice = fields.Boolean(related='partner_id.sport_practice')
    sport_id = fields.Many2one(related='partner_id.sport_id')
    sport_periodicity = fields.Selection(related='partner_id.sport_periodicity')
    personal_history_id = fields.Many2many(related='partner_id.personal_history_id')
    familiar_history_id = fields.Many2many(related='partner_id.familiar_history_id')

    @api.multi
    def unlink(self):
        """
        Ensure that the templates can't be deleted
        """
        template_id = self.env.ref("physiotherapy_mgmt.template_%s" % self._table)
        is_template = template_id.id == self.id

        if is_template:
            raise ValidationError(_('Template record can\'t be deleted!!'))
        return super().unlink()

    @api.multi
    def _default_values(self, var):
        # item = self.env.ref('physiotherapy_mgmt.template_{0}'.format(self._table))
        # item = self.env
        item = self.env[self._name].search([('active', '=', False)], limit=1)

        if item:
            var_type = item.fields_get().get(var).get('type')
            if var_type not in ('one2many', 'many2one', 'many2many'):
                return item.mapped(var)[0]
            elif var_type == 'many2one':
                return item.mapped(var).id
            elif var_type == 'many2many':
                return [(6, False, item.mapped(var).ids)]
            else:
                copy_ids = list()
                for register in item.mapped(var):
                    new_id = register.copy()
                    new_id.write({var: False})
                    copy_ids.append(new_id.id)
                return [(6, False, copy_ids)]


