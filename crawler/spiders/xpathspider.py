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
from urllib import urlencode
import json
import random
import re
import sys
import time
import traceback
from crawler.utils.urlutils import UrlUtils

reload(sys)
sys.setdefaultencoding( "utf-8" )

class ChannelSpider(BaseSpider):
    name = "xpathSpider"
    id = "xpathSpider"

    def __init__(self, id='xpathSpider'):
        self.rules = rules.rules
        self.seeds = json.JSONDecoder('utf-8').decode(''.join(open(settings.get('SEEDS')).readlines()))
        self.id = id
        self.start_urls = []
        self.ts = datetime.now()
        self.domain = settings.get('DOMAIN')
        self.seed = self.seeds.get(self.domain)
        self.rule = self.rules.get(self.domain)
        self.keys = {}
        self.urlutil = UrlUtils()
        self.getQueryWord()

    def getQueryWord(self):
        for url, key in self.seed.items():
            self.keys[url] = key
            self.start_urls.append(url)

    def make_requests_from_url(self, url):
        meta = {'url':url}
        if (settings.getbool("ENABLE_PROXY",False)):
            meta['proxy'] = settings.get('PROXY')
        return Request(url, dont_filter=True, meta = meta)
    
    def get_source_info(self, url, root):
        # result keyset {source, category, url, rss[, date, describe]}
        res = {}
        if root is None:
            self.log("Could not parse page: %s "% url, log.WARNING)
            return res
    
        nodes = root.xpath(self.rule['nodes'])
        if not nodes:
            self.log("Parse not result: %s"%url, log.WARNING)
            return res
    
        results = []
        for node in nodes:
            result = {}
            for key,r in self.rule['fields'].items():
                fnodes = node.xpath(r['xpath'])
                if not fnodes:
                    continue
                res = ""
                if isinstance(fnodes[0], etree._ElementUnicodeResult) or \
                        isinstance(fnodes[0], etree._ElementStringResult) :
                    res = ''.join(fnodes).strip()
                elif isinstance(nodes[0], etree._Element):
                    res = ''.join([etree.tounicode(n).strip() for n in fnodes])
                else:
                    self.log("xpath error: donot handle new node type %s, %s\n"%(type(nodes[0]), url), log.WARNING)
                    continue
    
                p = r.get('re')
                if p:
                    m = p.match(res)
                    if m:
                        res = m.group(1)
    
                result[key] = res
            
            result['category'] = self.keys[url]
            if "url" not in result:
                self.log("Could not parse url, skip: " + url, log.WARNING)
                continue
            results.append(result)
    
        self.log("Parse %d result from %s"%(len(results), url), log.INFO)
        return results  
    
    def get_page(self, root, url):
        res = None
        next_page = self.rule.get("next")
        if next_page is None:
            return res
        ns = root.xpath(next_page["xpath"])
        
        end_page = self.rule.get("end")
        ep = None
        if end_page is not None:
            ep = root.xpath(end_page["xpath"])
        
        res = None
        rep = None
        if ns is not None and len(ns) > 0:
            href = ns[0].strip()
            res = self.urlutil.norm(url, href)
            
        if ep is not None and len(ep) > 0:
            href = ep[0].strip()
            rep = self.urlutil.norm(url, href)
        if res == rep :
            return None
        self.log(res, log.INFO)
        self.log(rep, log.INFO)
        return res
    
    def parse(self, response):
        items = []
        page = ""
        try:
            page = response.body_as_unicode()
        except Exception, e:
            self.log("get body error: %s"%response.url, log.ERROR)
            return

        meta = response.meta
        root = etree.HTML(page)
        url = meta['url']
        news_data = self.get_source_info(url, root);
        
        for d in news_data:
            cit = ChannelItem()
            cit['url'] = d['url']
            cit['source'] = d.get('source')
            cit['keyword'] = d.get('category')
            cit['rss'] = d.get('rss')
            items.append(cit)
            
        nexturl = self.get_page(root, url)
        if nexturl is not None:
            items.append(Request(nexturl, dont_filter=True, meta = meta))
        return items

    
