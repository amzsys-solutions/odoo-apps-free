# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Amzsys Technology Solutions Pvt Ltd.
# See LICENSE file for full copyright and licensing details.
from odoo import fields, models

class SaleOrderLineWizard(models.TransientModel):

    _name = 'sale.order.line.wizard'
    _description = 'sale order line wizard'

    def add_sale_product(self):
        active_id = self.env['sale.order'].browse(self._context.get('active_ids'))

        for products_id in self.sale_order_line_wizard.ids:

            active_id.write({
                'order_line':
                    [
                        (0, 0, {
                            'product_id': products_id,
                        })
                    ]
            })

    sale_order_line_wizard = fields.Many2many('product.template', 'product_wiz_relation')

#
# class PurchaseOrderLinewizard(models.TransientModel):
#     _name = 'purchase.order.line.wizard'
#     _description = 'purchase order line wizard'
#
#
#     def add_purchase_product(self):
#         active_id = self.env['purchase.order'].browse(self._context.get('active_ids'))
#
#         for products_id in self.purchase_order_wizard.ids:
#             active_id.write({
#                 'order_line':
#                     [
#                         (0, 0, {
#                             'product_id': products_id,
#                         })
#                     ]
#             })
#
#
#     purchase_order_wizard = fields.Many2many('product.template', 'purchase_wiz_relation')

