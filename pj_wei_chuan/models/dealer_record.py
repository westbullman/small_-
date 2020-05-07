# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError

class DealerRecord(models.Model):

    _name = 'dealer.record'
    _description = '经销商'

    sequence = fields.Integer('Sequence', default=1, help="Used to order. Lower is better.")
    business_license_image = fields.Binary(string='营业执照')
    qr_code = fields.Binary(string='邀请二维码')
    name = fields.Char(string='经销商名称')
    vat = fields.Char(string='统一社会信用代码')
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    mobile = fields.Char(string='手机')
    bianma = fields.Char(string='编码')
    partner_ids = fields.One2many('res.partner','dealer_id',string='渠道商')


    @api.one
    @api.constrains('bianma')
    def _check_bianma(self):
        if self.search_count([('bianma','=',self.bianma)]) >1:
            raise ValidationError(_("该编码已经存在,请更换!"))





