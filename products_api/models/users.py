# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
import uuid

class Users(models.Model):
	_inherit = 'res.users'

	api_key = fields.Char("API Key")

	def action_api_key(self):
		for user in self:
			user.api_key = uuid.uuid1().hex
