#!/usr/bin/env python
# coding: utf-8
import datetime
import time

import requests
from bs4 import BeautifulSoup

__author__ = "lightless"
__email__ = "root@lightless.me"


class KDLHASpider:
    def __init__(self):
        self.url = "http://www.kuaidaili.com/free/inha/"
        self.tag = "快代理-国内-高匿"
        self.type = "HTTP"
        self.result_queue = None

    def set_result_queue(self, result_queue):
        self.result_queue = result_queue

    def run(self):
        # http://www.kuaidaili.com/free/inha/1/ - http://www.kuaidaili.com/free/inha/10/
        raw_url = "http://www.kuaidaili.com/free/inha/{page}/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36"
        }
        t_result = []
        for page in xrange(1, 11):

            url = raw_url.replace("{page}", str(page))
            r = requests.get(url, headers=headers)
            raw_html = r.text
            soup = BeautifulSoup(raw_html, "lxml")

            for tr in soup.find_all("tr")[1:]:
                each_item = {}
                td = tr.find_all("td")

                # 检测更新日期，只爬取今日更新的IP列表
                update_date = td[6].get_text()
                update_timeArray = time.strptime(update_date, "%Y-%m-%d %H:%M:%S")
                update_timestamp = int(time.mktime(update_timeArray))

                today_date = datetime.date.today()
                today_timestamp = int(time.mktime(today_date.timetuple()))

                if update_timestamp < today_timestamp:
                    continue

                # 填充数据
                each_item['ip'] = td[0].get_text()
                each_item['port'] = td[1].get_text()
                each_item['type'] = td[2].get_text()
                each_item['location'] = td[4].get_text()
                each_item['time'] = filter(lambda ch: ch in '0123456789.', td[5].get_text().encode("utf8"))
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

