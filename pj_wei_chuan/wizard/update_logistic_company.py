# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UpdateLogisticCompany(models.TransientModel):
    _name = 'update.logistic.company'
    _description = '更新物流公司'

    @api.multi
    def confirm(self):
        print("更新物流公司信息")
