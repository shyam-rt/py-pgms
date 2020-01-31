from odoo import models, fields


class showroom(models.Model):
	_name = 'showroom.brand'
	_description = 'showroom.showroom'
	name=fields.Char("brand name")
	model_name = fields.One2many("showroom.showroom","brand")
