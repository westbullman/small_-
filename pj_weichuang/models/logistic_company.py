# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class LogisticCompany(models.Model):

    _name = 'logistic.company'
    _description = '物流公司'

    short_name = fields.Char(string='简称')
    name = fields.Char(string='物流公司名称')