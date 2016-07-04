#!/usr/bin/env python
# coding: utf-8
import logging

__author__ = "lightless"
__email__ = "root@lightless.me"


console = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] [(%(threadName)s)] [%(asctime)s] [%(filename)s:%(lineno)d] %(message)s", "%H:%M:%S")
console.setFormatter(formatter)

logger = logging.getLogger("ProxySpiderLogger")
logger.addHandler(console)
logger.setLevel(logging.DEBUG)
