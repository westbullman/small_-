# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json
import urllib3

class UpdateLogisticCompany(models.TransientModel):
    _name = 'update.logistic.company'
    _description = '更新物流公司'

    @api.multi
    def confirm(self):
        asstoken = self.env['wechat.interface'].get_token()
        #获取所有物流公司
        http = urllib3.PoolManager()
        url = "https://api.weixin.qq.com/cgi-bin/express/business/delivery/getall?access_token=" + 'asstoken'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        req = http.request('GET',
                           url,
                           headers=headers)
        my_dict = json.loads(req.data)



