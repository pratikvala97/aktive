# -*- coding: utf-8 -*-

from odoo import api, fields, models


class contacts_partner(models.Model):

    _inherit = "res.partner"

    gold_partner = fields.Boolean("Gold Partner")
    premium_partner = fields.Boolean("Premium Partner")
