from odoo import models, fields

class product(models.Model):
	_inherit = 'product.template'
	model=fields.Char()
	variant=fields.Char()

	