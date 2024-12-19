# -*- coding: utf-8 -*-
# from odoo import http


# class Eshop(http.Controller):
#     @http.route('/eshop/eshop', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eshop/eshop/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('eshop.listing', {
#             'root': '/eshop/eshop',
#             'objects': http.request.env['eshop.eshop'].search([]),
#         })

#     @http.route('/eshop/eshop/objects/<model("eshop.eshop"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eshop.object', {
#             'object': obj
#         })

