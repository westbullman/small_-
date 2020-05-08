# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError

class ProductCategory(models.Model):

    _inherit = 'product.category'

    image = fields.Binary(string='分类图片')