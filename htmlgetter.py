#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import sys
import requests
import requests.exceptions
from pyquery import PyQuery as pq
from lxml import etree
import time
import logging
import random

import Proxy

reload(sys)
sys.setdefaultencoding('utf-8')


class MyProxy:
    proxylist = []
    def __init__(self):
        f = open('proxylist')
        for lines in f:
            lines = lines.strip()
            self.proxylist.append(lines)

    def findproxy(self):
        random.shuffle(self.proxylist, random.random)
        for lines in self.proxylist:
            if Proxy.checkpro(lines) == 1:
                return lines
        return None

    def getter(self, link):
        def _getter(link):
            proxyip = self.findproxy()
            if proxyip is None:
                link = requests.get(link, timeout=100)
            else:
                link = requests.get(link, proxies=proxyip, timeout=100)
            return link.text.encode('utf-8')

        for _ in range(5):
        #    print 'getter'+link
            try:
                ret = _getter(link)
            except requests.ConnectionError:
                time.sleep(10)
                continue
            except requests.exceptions.Timeout:
                time.sleep(10)
                continue
            else:
                return ret
        raise requests.ConnectionError("Connection Error")


__all__ = ["getter"]

if __name__ == '__main__':
    print MyProxy().findproxy()

# vim: ts=4 sw=4 sts=4 expandtab
