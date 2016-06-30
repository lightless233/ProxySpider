#!/usr/bin/env python
# coding: utf-8
import time


class Spider2:
    def __init__(self):
        self.url = "http://www.site-digger.com/html/articles/20110516/proxieslist.html"

    def run(self):
        print "spider 2 running..."
        time.sleep(3)
        print "spider 2 end..."


def get_spider_class():
    return Spider2


