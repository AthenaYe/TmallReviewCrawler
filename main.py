#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import sys
import argparse

from get_proxy_list import get_proxies

reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    parser = argparse.ArgumentParser(
        description="Crawl comments from Tmall",
    )
    subparsers = parser.add_subparsers(title="Subcommands")

    parser_get_proxies = subparsers.add_parser('get-proxies', help='Get proxy list')
    parser_get_proxies.add_argument('listfile', nargs='?', default="proxylist", help="File to save proxy list")
    parser_get_proxies.set_defaults(func=get_proxies)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    import settings
    import logging.config
    logging.config.dictConfig(settings.LOGGING)

    main()

# vim: ts=4 sw=4 sts=4 expandtab
