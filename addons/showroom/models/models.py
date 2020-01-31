# -*- coding: utf-8 -*-

from odoo import models, fields


class showroom(models.Model):
    _name = 'showroom.showroom'
    _description = 'showroom.showroom'
    Bike_Name = fields.Char()
    brand= fields.Many2one("showroom.brand")
    model_name = fields.Char()
    variant_name=fields.Char()
