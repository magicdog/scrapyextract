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
                    },
         "b2b":     {
                     "nodes" : "//li[@onmouseout=\"this.className=' '\"]/a",
                     "fields": {
                                "url"     : { "xpath" : "./@href" },
                                "source"  : { "xpath" : "./@title" }
                               }
                    },
         "toocle":   {
                     "nodes" : "//td[@width='590']/table[3]//a[@class='blue']",
                     "fields": {
                                "url"     : { "xpath" : "./@href" },
                                "source"  : { "xpath" : "./text()"},
                               }
                    },
         "360hy":   {
                     "nodes" : "//a[text() != '']",
                     "fields": {
                                "url"     : { "xpath" : "./@href" },
                                "source"  : { "xpath" : "./text()"},
                               }
                    },
         "jianzhu":   {
                     "nodes" : "//div[@class='div_content_h2']/a",
                     "fields": {
                                "url"     : { "xpath" : "./@href" },
                                "source"  : { "xpath" : "./text()"},
                               }
                    },
         "zgw":   {
                     "nodes" : "//div[@class='cmInner regList']//a | //div[@class='cmInner extend']//td[@class='c']//a",
                     "fields": {
                                "url"     : { "xpath" : "./@href" },
                                "source"  : { "xpath" : "./@title"},
                               }
                    },
         "lvse":
                    {
                     "nodes" : "//div[@class='info']/h2",
                     "fields": {
                                "url"     : { "xpath" : "./a[2]/@href" },
                                "source"  : { "xpath" : "./a[1]/text()"    },
                               },
                     "next"  : {  "xpath" : u"//a[@class='next' and contains(text(),'下一页')]/@href" }
                    },
          "caijing":
                    {
                     "nodes" : "//table[@id='tab_s']//a",
                     "fields": {
                                "url"     : { "xpath" : "./@href" },
                                "source"  : { "xpath" : "./text()"    },
                               }
                    },
          "junshi":
                    {
                     "nodes" : "//div[@class='jspd_4']//a",
                     "fields": {
                                "url"     : { "xpath" : "./@href" },
                                "source"  : { "xpath" : "./text()"    },
                               }
                    },
          "daxue":
                    {
                     "nodes" : "//td//p//a",
                     "fields": {
                                "url"     : { "xpath" : "./@href" },
                                "source"  : { "xpath" : "./text()"    },
                               }
                    }
       }
