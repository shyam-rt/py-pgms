
from odoo import models, fields


class showroom(models.Model):
	_name = 'showroom.model'
	_description = 'showroom.showroom'
	name = fields.Char("model name")
	variant_name=fields.Many2one("showroom.variant")