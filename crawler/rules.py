#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re

rules = { "feedex": {
                     "nodes" : "//div[@class='post']",
                     "fields": {
                                "url"     : { "xpath" : ".//small/a[5]/@href" },
                                "rss"     : { "xpath" : ".//small/a[3]/@href",
                                             "re"    : re.compile(r".*url=(.*)")
                                            },
                                "source"  : { "xpath" : ".//h2//text()"    },
                                "date"    : { "xpath" : ".//small//text()",
                                             "re"    : re.compile(r".*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")
                                            },
                                "describe": { "xpath" : ".//div[@class='entry']/text()"}
                               },
                     "next"  : {  "xpath" : "//div[@id='navi']/a[text()='Next']/@href" }
                    },
         "china_dmoz": 
                    {
                     "nodes" : "//div[@class='listbox']",
                     "fields": {
                                "url"     : { "xpath" : "./address/text()" },
                                "source"  : { "xpath" : "./h4/@title"    },
                                "describe": { "xpath" : "./p/text()"}
                               },
                     "next"  : {  "xpath" : "//span[@class='cur-page']/../../following-sibling::*[1]//a/@href" },
                     "end"   : {  "xpath" : u"//div[@class='page-num']/a[text()='最后一页']/@href" }
                    },
         "dzhai":
                    {
                     "nodes" : "//div[@class='listbox']",
                     "fields": {
                                "url"     : { "xpath" : "./address/text()" },
                                "source"  : { "xpath" : "./h4/a/text()"    },
                                "describe": { "xpath" : "./p/text()"}
                               },
                     "next"  : {  "xpath" : "///div[@class='PageNumbers']/child::span/following-sibling::*[1]//@href" }
                    }
       }
