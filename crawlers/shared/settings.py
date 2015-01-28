#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import sys
import os

LOG_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__name__), "log")
)

LOGGING = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'stream': sys.stdout,
        },
        'logfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOG_PATH, 'info_log'),
        },
        'errfile': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOG_PATH, 'error_log'),
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'logfile', 'errfile'],
            'level': 'INFO',
        },
    },
}


# vim: ts=4 sw=4 sts=4 expandtab
