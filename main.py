#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import sys
import argparse
import settings
import logging
import logging.config

from get_proxy_list import get_proxies
from tmall_crawler import TmallCrawler

reload(sys)
sys.setdefaultencoding('utf-8')


def crawl_tmall(args):
    tmall = TmallCrawler()
    tmall.get_comments(args.item_id)


def main():
    parser = argparse.ArgumentParser(description="Crawl comments from Tmall")
    parser.add_argument("--debug", action="store_true", help="Print debug info")

    subparsers = parser.add_subparsers(title="Subcommands")
    p_get_proxies = subparsers.add_parser('get-proxies', help='Get proxy list')
    p_get_proxies.add_argument(
        '-f', '--listfile',
        default="proxylist",
        help="File to save proxy list"
    )
    p_get_proxies.set_defaults(func=get_proxies)

    p_tmall = subparsers.add_parser('tmall', help='Get tmall comments for a item')
    p_tmall.add_argument(
        'item_id', help="Item id"
    )
    p_tmall.set_defaults(func=crawl_tmall)

    args = parser.parse_args()
    if args.debug:
        settings.LOGGING['handlers']['default']['level'] = "DEBUG"

    logging.config.dictConfig(settings.LOGGING)
    args.func(args)

if __name__ == "__main__":

    main()

# vim: ts=4 sw=4 sts=4 expandtab
