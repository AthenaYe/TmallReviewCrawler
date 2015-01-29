#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import json


def create_json(f, **kwargs):
    f.write(json.dumps(kwargs, encoding='UTF-8', ensure_ascii=False))
    f.write('\n')

# vim: ts=4 sw=4 sts=4 expandtab
