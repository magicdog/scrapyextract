
from __future__ import with_statement
import os
import sys
from urlparse import urlparse
from urlparse import urljoin
from urlparse import urlunparse
import posixpath


class UrlUtils:
    def __init__(self):
        # load tlds, ignore comments and empty lines:
        path = os.path.split(os.path.realpath(__file__))[0]
        with open(os.path.join(path, "effective_tld_names.dat")) as tld_file:
             self.tlds = [line.strip() for line in tld_file if line[0] not in "/\n"]
     
    def get_domain(self, url):
        url_elements = urlparse(url)[1].split('.')
        # url_elements = ["abcde","co","uk"]

        for i in range(-len(url_elements), 0):
            last_i_elements = url_elements[i:]
            #    i=-3: ["abcde","co","uk"]
            #    i=-2: ["co","uk"]
            #    i=-1: ["uk"] etc

            candidate = ".".join(last_i_elements) # abcde.co.uk, co.uk, uk
            wildcard_candidate = ".".join(["*"] + last_i_elements[1:]) # *.co.uk, *.uk, *
            exception_candidate = "!" + candidate

            # match tlds: 
            if (exception_candidate in self.tlds):
                return ".".join(url_elements[i:]) 
            if (candidate in self.tlds or wildcard_candidate in self.tlds):
                return ".".join(url_elements[i-1:])
                # returns "abcde.co.uk"    
    
    def norm(self, base, url):
        part = urlparse(url)
        if not part.scheme: 
            join = urljoin(base.strip(),url)
            url = urlparse(join)
            path = posixpath.normpath(url[2])
            #drop fragment
            res = urlunparse((url.scheme,url.netloc,path,url.params,url.query, ''))
        elif part.scheme == 'http':
            res = url 
        return res

if __name__ == '__main__':
    urlutils = UrlUtils()
    print urlutils.get_domain(sys.argv[1])
