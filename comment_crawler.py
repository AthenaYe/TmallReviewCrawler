#!/usr/bin/env python2
# -*- coding:utf-8 -*-


class CrawlException(Exception):
    """\
    Exception
    """
    pass


class CommentCrawler(object):
    """\
    A virtual class as the parent of all crawlers
    """

    def save(self, comment):
        """\
        Save comment

        Args:
            comment
        """
        raise Exception("Not Implemented!")

# vim: ts=4 sw=4 sts=4 expandtab
