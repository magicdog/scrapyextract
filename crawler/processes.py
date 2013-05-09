#!/usr/bin/env python
#-*- coding:utf-8 -*-

#add domain and suffix to the existed result, this file is used for the early crawls result,
#if using the scrapy to crawl now, we do not need this file
import os
import sys
from utils.urlutils import UrlUtils
from pymongo import Connection

class Processor():
    def __init__(self):
        self.urlutils = UrlUtils()
        self.conn = Connection('10.127.10.37')
        self.domains = {}
        for r in self.conn.crawldb.site.find():
            self.domains[r['_id']] = 1
    
    def process(self, file_path):
        if not os.path.exists(file_path) and not os.path.isfile(file_path):
            print "file not exits %s" % file_path
            return
        file_object = open(file_path, 'r')
        for line in file_object.readlines() :
            if line is None or len(line) < 3:
                continue
            fields = line.strip().split("\t")
            source = fields[0]
            category = fields[1]
            url = fields[2]
            
            domain = self.urlutils.get_domain(url)
            suffix = ''
            if domain in self.domains:
                suffix = 'y'
            if len(fields) == 4 :
                rss = fields[3]
                print "%s\t%s\t%s\t%s\t%s\t%s" % (source,category,url,domain,rss,suffix)
            else:
                print "%s\t%s\t%s\t%s\t%s" % (source,category,url,domain,suffix)
        return
            

processor = Processor()
processor.process(sys.argv[1])
        