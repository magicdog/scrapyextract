# Scrapy settings for channel project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'crawler'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29'
REFERER = 'http://ctrlq.org/rss/'

ITEM_PIPELINES = [
            'crawler.pipelines.FilterPipeline',
                ]

SEEDS = '/home/shelton/workspace/SpecificPageSpider/crawler/seeds'

DOWNLOAD_DELAY = 0.5
DOWNLOAD_TIMEOUT = 180
CONCURRENT_REQUESTS_PER_DOMAIN = 5
CONCURRENT_REQUESTS = 100
CONCURRENT_ITEMS = 200
#LOG_LEVEL = 'ERROR'
LOG_LEVEL = 'DEBUG'
#LOG_FILE = 'log'
LOG_STDOUT = True

# REDIS_HOST= '10.127.10.73'

ENABLE_PROXY = True
PROXY = 'http://10.127.10.42:3180'

MAX_MONGO_RECONNECT_ATTEMPTS = 3


KEYWORD_FETCH_INTERVAL_HOURS = 24
# CHANNEL_KEYWORD_URL = 'http://10.127.10.66:8030/service/global/doc_count?count=50'

# CTRLQ_URL = 'http://www.google.com/uds/GfindFeeds?q=%s&key=ABQIAAAA6C4bndUCBastUbawfhKGURTFnqBuwPowtiyJohQxh-8vJXk-MBTetbTPnQAbLgs9lUkeE34hNbC15Q&hl=zh_CN&v=1.0'
# DOMAIN = 'dzhai'

# DOMAIN = 'b2b'
DOMAIN = 'daxue'
# CHANNELSTAT_DATABASE_INFO = {
#     'host' : '10.127.10.37,10.127.10.68,10.127.10.23',
#     'table' : {
#         'lastInsertTime' : 'channel$lastInsertTime',
#         'keywords' : 'channel$keywords',
#         'queryWords' : 'channel$queryWords',
#         "urls" : "channel$urls",
#         "source" : "channel$source",
#         "blacklist" : "crawl$blacklist"
#     }
# }



DOWNLOADER_MIDDLEWARES_BASE = {
    'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware': 100,
    #'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': 300,
    'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
        
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
    'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': 550,
    

    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
    #'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware': 800,
    'scrapy.contrib.downloadermiddleware.chunked.ChunkedTransferMiddleware': 830,
    'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 850,
    #'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 900,
}

#MAIL_FROM = 'wj@hipu.com'
#MAIL_HOST = 'smtp.hipu.com'
#MAIL_USER = 'wj@hipu.com'
#MAIL_PASS = 'Hipu2012!@#'
MAIL_TO = 'wj@hipu.com'

DEFAULT_RESPONSE_ENCODING="gb18030"
ENCODING_ALIASES = {
        # gb2312 is superseded by gb18030
    'gb2312': 'gb18030',
    'chinese': 'gb18030',
    'csiso58gb231280': 'gb18030',
    'euc- cn': 'gb18030',
    'euccn': 'gb18030',
    'eucgb2312-cn': 'gb18030',
    'gb2312-1980': 'gb18030',
    'gb2312-80': 'gb18030',
    'iso- ir-58': 'gb18030',
        # gbk is superseded by gb18030
    'gbk': 'gb18030',
    '936': 'gb18030',
    'cp936': 'gb18030',
    'ms936': 'gb18030',
        # latin_1 is a subset of cp1252
    'latin_1': 'cp1252',
    'iso-8859-1': 'cp1252',
    'iso8859-1': 'cp1252',
    '8859': 'cp1252',
    'cp819': 'cp1252',
    'latin': 'cp1252',
    'latin1': 'cp1252',
    'l1': 'cp1252',
        # others
    'zh-cn': 'gb18030',
    'win-1251': 'cp1251',
    'macintosh' : 'mac_roman',
    'x-sjis': 'shift_jis',
}
