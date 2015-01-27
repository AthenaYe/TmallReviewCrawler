#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import logging
from httpclient import HTTPClient
from pyquery import PyQuery as pq

logger = logging.getLogger(__name__)


def get_proxies(args):

    clt = HTTPClient()
    f = open(args.listfile, 'w')
    proxylist, _ = clt.get('http://cn-proxy.com/', use_proxy=False)
    logger.info("Fetched proxy list page")
    proxylist = pq(proxylist)

    proxylist = proxylist('table[class="sortable"]')
    list1 = pq(proxylist[0])('td')
    list2 = pq(proxylist[1])('td')

    def printlist(l, f):
        i = 0
        for lines in l:
            if i % 5 == 0 and i!=0:
                f.write(pq(lines).text()+':')
            elif i % 5 == 1 and i!= 1:
                f.write(pq(lines).text()+'\n')
            i+=1

    printlist(list1, f)
    printlist(list2, f)
    f.close()
    logger.info("Done!")

__all__ = ["get_proxies"]

# vim: ts=4 sw=4 sts=4 expandtab
