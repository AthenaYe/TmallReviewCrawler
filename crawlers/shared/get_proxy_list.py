#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import logging
from .httpclient import HTTPClient
from pyquery import PyQuery as pq


def get_proxies(args):
    logger = logging.getLogger(__name__)
    if args.debug:
        logger.setLevel("DEBUG")

    list_url = 'http://cn-proxy.com/'

    clt = HTTPClient()
    f = open(args.listfile, 'w')

    logger.debug("Fetching proxy from {} to {}".format(
        list_url, args.listfile
    ))

    proxylist, _ = clt.get(list_url, use_proxy=False)
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
