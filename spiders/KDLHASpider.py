#!/usr/bin/env python
# coding: utf-8

__author__ = "lightless"
__email__ = "root@lightless.me"


class KDLSpider:
    def __init__(self):
        self.url = "http://www.kuaidaili.com/free/inha/"
        self.type = "HTTP"
        self.result_queue = None

    def set_result_queue(self, result_queue):
        self.result_queue = result_queue

    def run(self):
        # http://www.kuaidaili.com/free/inha/1/ - http://www.kuaidaili.com/free/inha/10/
        pass


def get_spider_class():
    return KDLSpider

