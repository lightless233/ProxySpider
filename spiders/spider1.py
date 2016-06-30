#!/usr/bin/env python
# coding: utf-8
import time

__author__ = "lightless"
__email__ = "root@lightless.me"

"""
爬虫插件类

命名规则：
      文件名与类名相同。

实现函数：
      __init__
            构造函数
      run
          爬取函数，返回值为列表，第一项为字典，存储基本信息，第二项为列表，其中每一项均为字典，
          字典中应当包括：ip，port，type，location，time
          ip： 代理地址的IP
          port： 代理地址的端口
          type： 代理类型，一般为 "透明，匿名，高匿" 其中之一，根据自己爬取的结果填充，若所爬页面未提供该值，填充为None即可。
          location： 该代理IP的位置，根据自己爬取的结果进行填充，若所爬页面未提供该值，填充为None即可。
          time： 该代理IP的响应时间，单位为秒。
          返回值格式如下：
          [
            {"url": self.url, "type": self.type},
            [
                {"ip": "33.44.55.66", "port": "80", "type": "高匿", "location": "中国 江苏省 苏州市 电信", "time": "0.3"},
                {"ip": "11.22.33.44", "port": "3128", "type": "透明", "location": "中国 河南省 洛阳市 电信", "time": "2.7"},
                {"ip": "22.33.44.55", "port": "8888", "type": "匿名", "location": "Taiwan", "time": "5.6"},
                ...
            ]
          ]
      set_result_queue
          设置结果队列，复制example中的函数即可，一般不需要修改。

      类外实现函数：get_spider_class
          返回爬虫类，按照example中的写法即可。
"""


class ExampleSpider:
    def __init__(self):
        # 待爬取的URL
        self.url = "Your url here."
        # 代理类型，包括HTTP，shadowsocks，VPN
        self.type = "HTTP"
        # Result Queue
        self.result_queue = None

    def set_result_queue(self, result_queue):
        self.result_queue = result_queue

    def run(self):
        # TODO: Add your process here...
        print "spider 1 running..."
        time.sleep(2)
        print "spider 1 end..."
        t = []
        s = {"ip": "11.22.33.44", "port": "8080", "type": u"透明", "location": u"Taiwan", "time": "2.6"}
        t.append(s)
        s = {"ip": "22.33.44.55", "port": "3128", "type": u"高匿", "location": u"江苏省南京市 联通", "time": "5"}
        t.append(s)
        tt = [{
            "url": self.url,
            "type": self.type,
        }, t]
        self.result_queue.put(tt)


def get_spider_class():
    return ExampleSpider

