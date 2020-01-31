
from odoo import models, fields


class showroom(models.Model):
	_name = 'showroom.variant'
	_description = 'showroom.showroom'
	name = fields.Char("variant_name")
	model_name = fields.One2many("showroom.model","variant_name")