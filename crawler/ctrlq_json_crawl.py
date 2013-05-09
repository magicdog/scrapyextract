#!/usr/bin/env python
#-*- coding:utf-8 -*-
from base_crawl import base_crawl
from urllib import urlencode
import json
import random
import time
import urllib2

class ctrlq_json_crawl(base_crawl):
    def __init__(self, output_file='result'):
        base_crawl.__init__(self, output_file)
        self.result_file = open(self.output_file, 'w+')
        
    def request(self, url):
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linuxx86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.16 Safari/534.24',
                  'Referer'   : 'http://ctrlq.org/rss/'}
        print 'Processing "%s" ...'%url
        req = urllib2.Request(url, headers=header)
        time.sleep(random.randint(1,6))
        resp = urllib2.urlopen(req).read()
        return resp
    
    def format_json(self, json_object):
       
        # result keyset {source, category, url, rss[, date, describe]}
        results= []
        if json_object is None:
            return results
        status      = json_object["responseStatus"]
        data        = json_object["responseData"]
        category    = data["query"]
        entries     = data["entries"]
        if status != 200:
            print "Status is not 200, but " + status + "query: "+category
            return results
        for entry in entries:
            result = {}
            result["source"] = entry["title"].replace("<b>", "").replace("</b>","")
            result["category"] = category
            result["url"] = entry["link"]
            result["rss"] = entry["url"]
            if "url" not in result:
                print "Could not parse url, skip: " + entry["link"]
                continue
            results.append(result)
        return results
        
    def crawl(self, url):
        # "http://.../html : [key1,key2..]" => url,categories
        json_str = self.request(url)
        json_object = json.JSONDecoder('utf-8').decode(json_str)
        res = self.format_json(json_object)
        self.write_to_file(self.result_file, res)
        
    def __del__(self):
        self.result_file.close()