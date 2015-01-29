__author__ = 'athena'
from crawlers.shared import httpclient
from crawlers.tmalldir.tmall_crawler import TmallCrawler
import os
from tinydb import TinyDB, where

def init_shop_items(shop_name):
    tmall = TmallCrawler()
    tmall.get_shopid(shop_name)
    product_db = TinyDB('tinydb_info/product_db.json')
    for ids in tmall.item_list:
        if not product_db.search(where('product_name')==ids):
            product_db.insert({'shop_type':'tmall',
                           'shop_name':shop_name,
                           'product_id':ids, 'if_visited':False})
    return

def init_shops():
    f = open('util/shop_name', 'r')
    for shop_name in f:
        print shop_name
        shop_name = shop_name.strip()
        shop_db = TinyDB('tinydb_info/shop_db.json')
        if not shop_db.search(where('shop_name')==shop_name):
            shop_db.insert({'shop_type':'tmall', 'shop_name':shop_name, 'if_visited':False})
    f.close()
    return

def init_shop_to_items():
    shop_db = TinyDB('tinydb_info/shop_db.json')
    shop_list = shop_db.search(where('if_visited')==False)
    for shop_info in shop_list:
        shop_name = shop_info['shop_name']
        init_shop_items(shop_name)
        shop_db.update({'if_visited':True}, where('shop_name')==shop_name)
    return

def test_proxy():
    aa = httpclient.HTTPClient()
    print aa.find_proxy()

def online_crawler():
    tmall = TmallCrawler()
    product_db = TinyDB('tinydb_info/product_db.json')
    product_list = product_db.search(where('if_visited')==False)
    for product_info in product_list:
        tmall.get_comments(product_info['product_id'])
        product_db.update({'if_visited':True}, where('product_id')==product_info['product_id'])
    return

if __name__=='__main__':
    init_shops()
    init_shop_to_items()
    online_crawler()
#    init_shop_items()