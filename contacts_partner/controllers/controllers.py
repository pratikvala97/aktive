# -*- coding: utf-8 -*-
# from odoo import http


# class ContactsPartner(http.Controller):
#     @http.route('/contacts_partner/contacts_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contacts_partner/contacts_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contacts_partner.listing', {
#             'root': '/contacts_partner/contacts_partner',
#             'objects': http.request.env['contacts_partner.contacts_partner'].search([]),
#         })

#     @http.route('/contacts_partner/contacts_partner/objects/<model("contacts_partner.contacts_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contacts_partner.object', {
#             'object': obj
#         })
