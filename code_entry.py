__author__ = 'athena'
from crawlers.shared import httpclient
from crawlers.tmalldir.tmall_crawler import TmallCrawler

tmall = TmallCrawler()
shop_name = 'chipisheaumeiu'
#tmall.get_shopid(shop_name)
#f = open('util/shop_name_'+shop_name, 'w')
#for ids in tmall.item_list:
#    f.write(ids + '\n')
#f.close()
f = open('util/shop_name_'+shop_name, 'r')
for lines in f:
    lines = lines.strip()
    tmall.get_comments(lines)
f.close()
#aa = httpclient.HTTPClient()
#print aa.find_proxy()
