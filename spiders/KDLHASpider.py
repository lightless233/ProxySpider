#!/usr/bin/env python
# coding: utf-8
import os

from bs4 import BeautifulSoup
from selenium import webdriver

__author__ = "lightless"
__email__ = "root@lightless.me"


class KDLHASpider:
    def __init__(self):
        self.url = "http://www.kuaidaili.com/free/inha/"
        self.tag = "快代理-每日更新"
        self.type = "HTTP"
        self.result_queue = None
        self.phantomjs_path = None

    def set_result_queue(self, result_queue):
        self.result_queue = result_queue

    def run(self):
        # http://www.kuaidaili.com/proxylist/1/
        raw_url = "http://www.kuaidaili.com/proxylist/{page}/"

        t_result = []
        for page in xrange(1, 11):
            url = raw_url.replace("{page}", str(page))
            print url
            driver = webdriver.PhantomJS(executable_path=self.phantomjs_path)
            driver.get(url)
            raw_html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

            soup = BeautifulSoup(raw_html, "html5lib")
            for tr in soup.find_all("tr")[1:]:
                each_item = {}
                td = tr.find_all("td")

                # 填充数据
                each_item['ip'] = td[0].get_text()
                each_item['port'] = td[1].get_text()
                each_item['type'] = td[2].get_text()
                each_item['protocol'] = td[3].get_text().replace(", ", "-")
                each_item['location'] = td[5].get_text()
                each_item['time'] = filter(lambda ch: ch in '0123456789.', td[6].get_text().encode("utf8"))
                t_result.append(each_item)
        # 填充结果集
        result = []
        info = dict()
        info['url'] = self.url
        info['type'] = self.type
        info['tag'] = self.tag
        result.append(info)
        result.append(t_result)
        self.result_queue.put(result)


def get_spider_class():
    return KDLHASpider

