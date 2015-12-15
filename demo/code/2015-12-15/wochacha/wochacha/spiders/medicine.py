# -*- coding: utf-8 -*-
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from .items import MedicineItem


class MedicineSpider(CrawlSpider):
    name = "medicine"
    allowed_domains = ["wochacha.com"]
    start_urls = (
        'http://android.wochacha.com/medicine/',
    )
    rules = (
        Rule(LinkExtractor(allow=('/medicine/class/id/', ))),
        Rule(LinkExtractor(allow=('/medicine/search/query/*', ))),
        Rule(LinkExtractor(allow=(r'/medicine/search/query/.*/page/\d+', ))),
        Rule(LinkExtractor(allow=('/medicine/brand',))),
        Rule(LinkExtractor(allow=('/medicine/manu/pkid/',)),
             callback='parse_item'),
    )

    def parse_item(self, response):
        item = MedicineItem()
        ret = response.xpath('//div[@class="tli"]/text()')
        ret = [i.extract().strip() for i in ret]
        name_map = {
            u'商品名': 'name',
            u'厂家': 'manufacturer',
            u'规格': 'size',
            u'剂量': 'dosage',
            u'批准文号': 'approval_number',
            u'条形码': 'barcode'}
        #  格式:
        #  [name]value
        reg = r'\[(.*)\](.*)'
        for s in ret:
            m = re.match(reg, s)
            if m is not None:
                k, v = m.group(1), m.group(2)
                if k in name_map:
                    item[name_map[k]] = v
        return item
