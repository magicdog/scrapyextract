# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import re
import time
import json
import traceback
from scrapy import log
from scrapy.conf import settings
from scrapy import signals
from datetime import timedelta
from datetime import datetime
from scrapy.exceptions import DropItem
from scrapy.xlib.pydispatch import dispatcher
from datetime import date
from crawler.utils.urlutils import UrlUtils
from pymongo import Connection

class FilterPipeline(object):
    def __init__(self):
        self.urlutils = UrlUtils()
        self.outputfile = {}
        self.conn = Connection('10.127.10.37')
        self.domains = {}
        for r in self.conn.crawldb.site.find():
            self.domains[r['_id']] = 1
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def __del__(self):
        pass

    def spider_opened(self, spider):
        result_file = open(spider.id + str(date.today()), 'w+')
        self.outputfile[spider.id] = result_file

    def spider_closed(self, spider):
        file = self.outputfile.get(spider.id)
        if file is not None:
            self.outputfile[spider.id].close()

    def process_item(self, item, spider):
        file = self.outputfile.get(spider.id)
        if file is not None:
            url = item["url"]
            if url.find("http://") == -1:
                url = "http://" + url
            domain = self.urlutils.get_domain(url)
            suffix = ''
            if domain in self.domains:
                suffix = 'y'
            rss = item["rss"]
            if rss is None:
                rss = ''
            line = "%s\t%s\t%s\t%s\t%s\t%s\n" %(item.get("source"), domain, item["keyword"],url,rss,suffix)
            file.write(line.encode("utf-8",'ignore'))
        return item
        

