#!/usr/bin/env python

from pymongo import Connection
import sys


conn = Connection('10.127.10.37')
#conn = Connection('192.168.1.13')


def dedup_filter():
    domains = {}
    for r in conn.crawldb.site.find():
        domains[r['_id']] = 1

    for line in open(sys.argv[1]).readlines():
        line = line.split('\n')[0] 
        parts = line.split('\t')
        domain = parts[1]
        suffix = ''
        if domain in domains:
            suffix = '\ty'
        print line + suffix 
 
dedup_filter()
sys.exit()

