__author__ = 'athena'
from crawlers.shared import httpclient
from crawlers.tmalldir.tmall_crawler import TmallCrawler

#tmall = TmallCrawler()
#tmall.get_comments(40272354595)
aa = httpclient.HTTPClient()
print aa.find_proxy()