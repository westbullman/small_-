# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError

class ProductProduct(models.Model):

    _inherit = 'product.product'

    images = fields.One2many('product.image','product_id',string='产品图片')
    hot_product = fields.Boolean(string='是否是热门产品', default=False)

    @api.one
    @api.constrains('default_code')
    def _check_default_code(self):
        if self.search_count([('default_code', '=', self.default_code)]) > 1:
            raise ValidationError(_("该产品编码已经存在,请更换!"))


class ProductImage(models.Model):

    _name = 'product.image'

    product_id = fields.Many2one('product.product',string='产品')
    sequence = fields.Integer('Sequence', default=1, help="Used to order. Lower is better.")
    image = fields.Binary(string='产品图片')


