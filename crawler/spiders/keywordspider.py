#!/usr/bin/env python
#-*- coding:utf-8 -*-

from crawler import rules
from crawler.items import ChannelItem
from datetime import datetime
from lxml import etree
from scrapy import log
from scrapy.conf import settings
from scrapy.exceptions import CloseSpider
from scrapy.http import Request
from scrapy.spider import BaseSpider
from urllib import quote
import json
import random
import re
import sys
import time
import traceback
from crawler.utils import urlutils

reload(sys)
sys.setdefaultencoding( "utf-8" )

class ChannelSpider(BaseSpider):
    name = "keywordSpider"
    id = "keywordSpider"

    def __init__(self, id='keywordSpider'):
        self.rules = rules.rules
        self.seeds = json.JSONDecoder('utf-8').decode(''.join(open(settings.get('SEEDS')).readlines()))
        self.id = id
        self.start_urls = []
        self.ts = datetime.now()
        self.domain = settings.get('DOMAIN')
        self.seed = self.seeds.get(self.domain)
        self.rule = self.rules.get(self.domain)
        self.getQueryWord()

    def getQueryWord(self):
        for url, keys in self.seed.items():
            self.start_urls.extend(keys)
        

    def make_requests_from_url(self, url):
        qurl =  settings.get("CTRLQ_URL") % quote(url)
        meta={'proxy':settings.get('PROXY')}
        return Request(qurl, dont_filter=True, meta = meta)
    def format_json(self, json_object):
        # result keyset {source, category, url, rss[, date, describe]}
        results= []
        if json_object is None:
            return results
        status      = json_object["responseStatus"]
        data        = json_object["responseData"]
        category    = data.get("query")
        entries     = data.get("entries")
        if status != 200:
            self.log("Status is not 200, but " + status + "query: "+category, log.WARNING)
            return results
        for entry in entries:
            result = {}
            result["source"] = entry["title"].replace("<b>", "").replace("</b>","")
            result["category"] = category
            result["url"] = entry["link"]
            result["rss"] = entry["url"]
            if "url" not in result:
                self.log("Could not parse url, skip: " + entry["link"], log.WARNING) 
                continue
            results.append(result)
        return results
    
    def parse(self, response):
        items = []
        page = ""
        try:
            page = response.body_as_unicode()
        except Exception, e:
            self.log("get body error: %s"%response.url, log.ERROR)
            return

        meta = response.meta
        news_data = self.format_json(json.JSONDecoder('utf-8').decode(page))
        
        for d in news_data:
            cit = ChannelItem()
            cit['url'] = d['url']
            cit['source'] = d.get('source')
            cit['keyword'] = d.get('category')
            cit['rss'] = d.get('rss')
            items.append(cit)

        return items

    
