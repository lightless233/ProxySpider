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
            self.add_function(fn)

    def add_function(self, func):
        if callable(func):
            self.__function_list.put(func)

    def run(self):
        # 从队列中获取工作函数
        while not self.__function_list.empty():
            fn = self.__function_list.get(block=True, timeout=1)
            t = threading.Thread(target=fn, name=str(fn.im_class).split(".")[-1])
            self.__thread_list.append(t)

        # 开始多线程运行工作函数
        for t in self.__thread_list:
            logger.debug("[*] " + t.getName() + " started.")
            t.start()
        for t in self.__thread_list:
            t.join()

    def print_functions(self):
        print self.__function_list
