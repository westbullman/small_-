# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
import hashlib
from datetime import datetime
import logging
import requests

# class PjBwy(http.Controller):
#     @http.route('/register', type='http', methods=['GET', 'POST'], auth='none', cors='*', csrf=False, website=True)
#     def get_userinfo(self, **kw):
#         return "sdasdad"
