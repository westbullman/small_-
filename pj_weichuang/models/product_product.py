# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductProduct(models.Model):

    _inherit = 'product.product'

    images = fields.One2many('product.image','product_id',string='产品图片')
    hot_product = fields.Boolean(string='是否是热门产品', default=False)
    _sql_constrains = [
        ("product_unique_product_id",
         "UNIQUE(product_id)",
         "产品编码必须唯一!"),
    ]


class ProductImage(models.Model):

    _name = 'product.image'

    product_id = fields.Many2one('product.product',string='产品')
    sequence = fields.Integer('Sequence', default=1, help="Used to order. Lower is better.")
    image = fields.Binary(string='产品图片')


