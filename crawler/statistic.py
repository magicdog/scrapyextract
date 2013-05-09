#!/usr/bin/env python
#-*- coding:utf-8 -*-
#caculate the repeated times according source .
import os
import sys
from utils.urlutils import UrlUtils

class Processor():
    def __init__(self):
        self.counts = {}
        self.lines = {}
    
    def process(self, file_path):
        if not os.path.exists(file_path) and not os.path.isfile(file_path):
            print "file not exits %s" % file_path
            return
        file_object = open(file_path, 'r')
        for line in file_object.readlines() :
            if line is None or len(line) < 3:
                continue
            source = line.split("\t")[0]
            self.lines[source] = line.strip("\r\n")
            self.counts[source] = self.counts.get(source,0) + 1
        for key,value in self.counts.items():
            print "%s\t%s" % (self.lines[key], value)
        return
            

processor = Processor()
processor.process(sys.argv[1])
# processor.process("./result/ctrl")
        