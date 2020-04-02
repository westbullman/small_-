# -*- coding: utf-8 -*-
{
    "name": "PJ Weichuang",
    "summary": "Application Weichuang",
    "version": "0.1",
    "category": "Weichuang",
    "website": "http://www.cotong.com",
    "author": "上海企通网络科技有限公司",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "mail",
        "product",
    ],
    "data": [
        "security/ir.model.access.csv",
        # "data/res_groups_data.xml",
        "views/product_product.xml",
        "views/dealer_record.xml",
        "views/menuitem.xml",
    ],
    # "demo": [
    #     'demo/export_demo.xml',
    #     'demo/ir.exports.line.csv',
    # ],
}