#!/usr/bin/env python
# coding: utf-8

import codecs

from utils.LoggerHelp import logger

__author__ = "lightless"
__email__ = "root@lightless.me"


def write_file(results_queue, thread_pool, filename="proxy-ip-list.csv"):
    logger.debug("write_file called.")
    with open(filename, "w") as ff:
        # 写入BOM头
        ff.write(codecs.BOM_UTF8)
        # 写入内容
        while not results_queue.empty() or not thread_pool.is_all_thread_dead():
            res = results_queue.get(block=True)
            ff.writelines(res[0].get('url') + "\n")
            ff.writelines("ip,port,type,protocol,location,time(s)\n")
            logger.info("[*] url: " + res[0].get('url'))
            res = res[1]
            for r in res:
                line = r.get('ip', 'None') + "," + r.get('port', 'None') + "," + \
                       r.get('type', 'None') + "," + r.get('protocol', 'None') + "," + \
                       r.get('location', 'None') + "," + r.get('time', 'None')
                logger.info("[*] " + line)
                ff.writelines((line+"\n").encode("utf8"))


