#!encoding=utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo
from pymongo.errors import AutoReconnect
from scrapy import log
from scrapy.mail import MailSender
import traceback

import functools
import time

MAX_AUTO_RECONNECT_ATTEMPTS = 3

def auto_reconnect(mongo_op_func):
    """Gracefully handle a reconnection event."""
    @functools.wraps(mongo_op_func)
    def wrapper(*args, **kwargs):
        max_attempts = settings.getint("MAX_MONGO_RECONNECT_ATTEMPTS", MAX_AUTO_RECONNECT_ATTEMPTS)
        mail = MailSender()
        for attempt in xrange(max_attempts):
            try:
                return mongo_op_func(*args, **kwargs)
            except AutoReconnect as e:
                wait_t = 1 + attempt # exponential back off
                log.msg("PyMongo auto-reconnecting... %s. Waiting %.1f seconds."%(str(e), wait_t), log.INFO)
                mail.send(to=[settings.get('MAIL_TO')], subject='PyMongo auto-reconnecting....', \
                      body="%s\n%s"%(e, traceback.format_exc()))
                time.sleep(wait_t)
    return wrapper

@auto_reconnect
def connection(*args, **kwargs):
    return pymongo.Connection(*args, **kwargs)
       
    
    
    