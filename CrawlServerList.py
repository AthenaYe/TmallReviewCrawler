#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import sys
import requests
import htmlgetter
from pyquery import PyQuery as pq


reload(sys)
sys.setdefaultencoding('utf-8')

f = open('proxylist', 'w')
proxylist = htmlgetter.getter('http://cn-proxy.com/')
proxylist = pq(proxylist)

proxylist = proxylist('table[class="sortable"]')
list1 = pq(proxylist[0])('td')
list2 = pq(proxylist[1])('td')

def printlist(l):
    i = 0
    for lines in l:
        if i % 5 == 0 and i!=0:
            f.write(pq(lines).text()+':')
        elif i % 5 == 1 and i!= 1:
            f.write(pq(lines).text()+'\n')
        i+=1

printlist(list1)
printlist(list2)


# vim: ts=4 sw=4 sts=4 expandtab
