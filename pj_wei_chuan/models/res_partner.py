# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
from odoo import api, fields, models


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    dealer_id = fields.Many2one('dealer.record',string='经销商')

    @api.model
    def search_render(self):
        print("=========")
        key = self.env['res.partner'].search(
            [('customer', '=', True), ('active', '=', 1),
             ('is_company', '=', 1)])
        print(key)
        datas = []
        for i in key:
            data = {
                'name': i.name,
                'state_id': i.state_id.name,
                'city': i.city,
                'street2': i.street2,
                'street': i.street,
                'phone': i.phone,
                'mobile': i.mobile
            }
            datas.append(data)
        return datas

