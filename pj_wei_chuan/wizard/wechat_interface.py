# -*- coding: utf-8 -*-
import datetime
import time
import json
import urllib3

from odoo import models, fields, api

class WechatInterface(models.TransientModel):
    _name = 'wechat.interface'
    _description = '微信小程序接口'

    @api.multi
    def get_token(self):
        appid = self.env.ref('pj_wei_chuan.wechat_appid').value
        secret = self.env.ref('pj_wei_chuan.wechat_secret').value
        #获取token的更新时间
        write_date = self.env.ref('pj_wei_chuan.wechat_access_token').write_date
        different_time = (datetime.datetime.now()-write_date)
        # 如果和现在相差的时间大于7000秒，重新获取token，不然就返回数据库的token
        if (different_time).seconds >7000:
            http = urllib3.PoolManager()
            url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=" + 'client_credential' + \
                  "&appid=" + appid + \
                  "&secret=" + secret
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            req = http.request('GET',
                               url,
                               headers=headers)
            my_dict = json.loads(req.data)
            self.env.ref('pj_wei_chuan.wechat_access_token').write({'value':str(my_dict['access_token'])})
            return str(my_dict['access_token'])
        else:
            return self.env.ref('pj_wei_chuan.wechat_access_token').value


