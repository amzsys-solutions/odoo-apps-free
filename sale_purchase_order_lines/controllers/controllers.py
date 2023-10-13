# -*- coding: utf-8 -*-
# from odoo import http


# class Multiproduct(http.Controller):
#     @http.route('/multiproduct/multiproduct/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/multiproduct/multiproduct/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('multiproduct.listing', {
#             'root': '/multiproduct/multiproduct',
#             'objects': http.request.env['multiproduct.multiproduct'].search([]),
#         })

#     @http.route('/multiproduct/multiproduct/objects/<model("multiproduct.multiproduct"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('multiproduct.object', {
#             'object': obj
#         })
