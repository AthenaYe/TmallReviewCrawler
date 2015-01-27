#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import sys
import requests
import requests.exceptions
import time
import logging
import random

reload(sys)
sys.setdefaultencoding('utf-8')


class HTTPClient(object):
    """
    This class implements HTTP GET request and supports HTTP proxy
    """

    proxylist = None
    logger = logging.getLogger("HTTPClient")

    @classmethod
    def init_proxylist(cls, list_filename="proxylist"):
        """
        @param list_filename: the file which stores proxies
        """
        if list_filename:
            with open(list_filename) as f:
                cls.proxylist = [line.strip() for line in f]
        else:
            raise Exception("Proxylist should be specified")

    def __init__(self, fail_interval=10):
        """
        @param fail_interval: time to sleep when connection error
        """
        self.fail_interval = fail_interval

        # TODO: getter deprecated
        self.getter = self.get

    @classmethod
    def checkpro(cls, line):
        line = line.strip()
        line = {'http': line}
        try:
            r = requests.get('http://www.baidu.com', proxies=line, timeout=5)
            print r.status_code
            if r.status_code == requests.codes.ok:
                return 1
                print('haha')
            else:
                print('wuwu')
                return 0
        except KeyboardInterrupt:
            raise
        except:
            cls.logger.exception("Got Exception")
        return 0

    def findproxy(self):
        random.shuffle(self.proxylist, random.random)
        for line in self.proxylist:
            if self.checkpro(line) == 1:
                return line
        return None

    def get(self, link, use_proxy=True):
        def _getter(link):
            kwargs = {
                'timeout': 100,
            }

            if use_proxy and self.proxylist is not None:
                proxyip = self.findproxy()
                if proxyip is not None:
                    kwargs['proxies'] = proxyip

            ret = requests.get(link, **kwargs)
            return ret.text.encode('utf-8'), ret.status_code

        for _ in range(5):
            # print 'getter'+link
            try:
                ret, status_code = _getter(link)
            except requests.ConnectionError:
                time.sleep(self.fail_interval)
                continue
            except requests.exceptions.Timeout:
                time.sleep(self.fail_interval)
                continue
            else:
                return ret, status_code
        raise requests.ConnectionError("Connection Error")


# For backward compabilities
MyProxy = HTTPClient


__all__ = ["HTTPClient", "MyProxy"]

if __name__ == '__main__':
    import settings
    import logging.config
    logging.config.dictConfig(settings.LOGGING)

    print MyProxy().findproxy()

# vim: ts=4 sw=4 sts=4 expandtab
