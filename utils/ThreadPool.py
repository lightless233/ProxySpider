#!/usr/bin/env python
# coding: utf-8

import Queue
import threading
from multiprocessing import cpu_count

from utils.LoggerHelp import logger

__author__ = "lightless"
__email__ = "root@lightless.me"


class ThreadPool:
    def __init__(self, thread_count=cpu_count()):
        self.__thread_count = thread_count
        self.__function_list = Queue.Queue(maxsize=0)
        self.__thread_list = []

    def add_function_list(self, function_list=[]):
        for fn in function_list:
            self.add_function(fn[0], **fn[1])

    def add_function(self, func, **kwargs):
        if callable(func):
            self.__function_list.put((func, kwargs))

    def run(self):
        # 从队列中获取工作函数
        while not self.__function_list.empty():
            fn = self.__function_list.get_nowait()
            try:
                thread_name = str(fn[0].im_class).split(".")[-1]
            except AttributeError:
                thread_name = fn[0].__name__
            t = threading.Thread(target=fn[0], name=thread_name, kwargs=fn[1])
            self.__thread_list.append(t)

        # 开始多线程运行工作函数
        for t in self.__thread_list:
            logger.debug("[*] " + t.getName() + " started.")
            t.start()
        for t in self.__thread_list:
            t.join()

    def print_functions(self):
        print self.__function_list
