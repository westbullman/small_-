# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SendGoods(models.TransientModel):
    _name = 'send.goods'

    logistic_company_id = fields.Many2one('logistic.company', string='物流公司')
    logistic_no = fields.Char(string='快递单号')

    @api.multi
    def confirm(self):
        context = dict(self._context or {})
        sale_order_id = context.get('active_ids')
        sale_order_object = self.env['sale.order'].search([('id','=',sale_order_id[0])])
        sale_order_object.write({'logistic_company_id':self.logistic_company_id.id,
                             'logistic_no':(self.logistic_no).strip()})
        print(sale_order_id)