#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import sys
import requests
import requests.exceptions
import time
import logging
import random


from . import settings     #no handlers should be found for httpclient?
import logging.config
logging.config.dictConfig(settings.LOGGING)

reload(sys)
sys.setdefaultencoding('utf-8')


class HTTPClient(object):
    """
    This class implements HTTP GET request and supports HTTP proxy
    """

    proxy_list = None
    logger = logging.getLogger("HTTPClient")

    @classmethod
    def init_proxylist(cls, list_filename="util/proxy_list"):
        """\
        Init proxylist from list file

        Args:
            list_filename: the file which stores proxies
        """
        if list_filename:
            with open(list_filename) as f:
                cls.proxy_list = [line.strip() for line in f]
        else:
            raise Exception("Proxy list should be specified")
    #    print cls.proxy_list

    def __init__(self, fail_interval=10):
        """\
        Args:
            fail_interval: time to sleep when connection error
        """
        self.fail_interval = fail_interval

    @classmethod
    def check_proxy(cls, candidate_proxy):
        candidate_proxy = candidate_proxy.strip()
        candidate_proxy = {'http': candidate_proxy}
        try:
            r = requests.get('http://www.baidu.com', proxies=candidate_proxy, timeout=5)
        #    print r.status_code
            if r.status_code == requests.codes.ok:
                return 1
            else:
                return 0
        except KeyboardInterrupt:
            raise
        except:
            cls.logger.exception("Got Exception")
            return 0
        return 0

    def find_proxy(cls):  #what if too many code access to it in the meantime?
        if not cls.proxy_list:
            cls.init_proxylist()
        random.shuffle(cls.proxy_list, random.random)
        for candidate_proxy in cls.proxy_list:
            if cls.check_proxy(candidate_proxy) == 1:
                return candidate_proxy
        return None

    def get(self, link, use_proxy=True, **kwargs):
        """\
        Args:

            link: the url to fetch
            use_proxy: whether to use proxy
            **kwargs: arguments to pass to `request.get`

        Returns:
            A tuple of (text, status_code)

            text: page content
            status_code: HTTP status code

        Raises:
            ConnectionError
        """

        def _getter(link):
            if 'timeout' not in kwargs:
                kwargs['timeout'] = 100

            if (use_proxy
               and self.proxy_list is not None
               and 'proxies' not in kwargs):
                # if use_proxy is false or self.proxylist not specified,
                # or 'proxies' has been specified by user,
                # leave alone

                proxyip = self.findproxy()
                if proxyip is not None:
                    kwargs['proxies'] = proxyip

            ret = requests.get(link, **kwargs)
            # return ret.text.encode('utf-8'), ret.status_code
            return ret.text, ret.status_code

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
    from . import settings
    import logging.config
    logging.config.dictConfig(settings.LOGGING)

    print HTTPClient().find_proxy()

# vim: ts=4 sw=4 sts=4 expandtab
