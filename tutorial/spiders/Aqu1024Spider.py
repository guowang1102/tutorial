#coding=utf-8

import re
import json
from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from tutorial.items import *


class Aqu1024Spider(CrawlSpider):
    name = "Aqu1024Spider"
    allowed_domains = ["1024.luj8le.net"]
    start_urls = [
        "http://1024.luj8le.net/pw/htm_data/3/1707/711823.html"
    ]
    rules = [  # 定义爬取URL的规则
            Rule(sle(allow=("/pw/htm_data/3/1707/71182[0-3].html")), follow=True, callback='parse_item')
    ]

    def parse_item(self, response):  # 提取数据到Items里面，主要用到XPath和CSS选择器提取网页数据
        items = []
        sel = Selector(response)
        #table = sel.css('div.t.t2')
        #table = sel.xpath('//div[@class ="tpc_content"]/text()').extract_first()

        #table = sel.xpath("//div[@class='tpc_content']//text()").extract_first()
        #table = response.xpath("//div[@class='tpc_content']").extract_first()
        table = response.xpath("//div[@class='tpc_content']//node()").extract_first()
        #table = response.xpath('//div[@class="tpc_content"]/*').extract()

        #table = response.xpath('//div[@class="tpc_content"]/*').extract_first()
        sites = table.split('<br><br><br><br>')
        for site in sites:
            print '--------------->sites is not null'
            item = Aqu1024Item()
            details = site.split('<br>')
            item['title'] = details[0]
        # print table.encode('utf-8')
        # for site in table:
        #     print '--------------->table is not null'
        #     item = Aqu1024Item()
        #     item['title'] = site.xpath("//img/@src").extract()[0]
        # #     # relative_url = site.css('.l.square a').xpath('@href').extract()[0]
        # #     # item['detailLink'] = urljoin_rfc(base_url, relative_url)
        # #     # item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()
        # #     # item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract()
        # #     # item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract()
        # #     # item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract()
        # #
        # #     # print site.css('h3 a').xpath('text()').extract()
        # #
            items.append(item)
            print repr(item).decode("unicode-escape") + '\n'

        # sites_odd = sel.css('table.tablelist tr.odd')
        # for site in sites_odd:
        #     item = Aqu1024Item()
        #     item['name'] = site.css('.l.square a').xpath('text()').extract()
        #     relative_url = site.css('.l.square a').xpath('@href').extract()[0]
        #     item['detailLink'] = urljoin_rfc(base_url, relative_url)
        #     item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()
        #     item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract()
        #     item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract()
        #     item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract()
        #     items.append(item)
            #print repr(item).decode("unicode-escape") + '\n'

        # info('parsed ' + str(response))

        return items
    def _process_request(self, request):
        # info('process ' + str(request))
        return request