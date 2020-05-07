# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    logistic_company_id = fields.Many2one('logistic.company',string='物流公司')
    logistic_no = fields.Char(string='快递单号')
    logistic_text = fields.Text(string='物流信息')