# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class contacts_wizard(models.AbstractModel):

	_inherit = "res.partner"


	def select_gold_partner(self):
		# selected_ids = self.env.context.get('active_ids', [])
		# selected_records = self.env['res.partner'].browse(selected_ids)
		raise ValidationError('selected name is',self.selected_records.display_name)
		# print("\n\n\n\n\n\nselectd gold ids",selected_records.display_name)
		# active_ids = self.ids
		# print("\n\n\n\n\nactive ids",active_ids.id.name)

		# for rec in self:

		# 	if rec.selected_records.id.name and rec.selected_records.id.type=='contact':
		# 		rec.gold_partner = True 
		# 	else:
		# 		raise ValidationError('selected name is',rec.selected_records.name)