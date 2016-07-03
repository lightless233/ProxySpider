#!/usr/bin/env python
# coding: utf-8
import codecs
import sys

from utils.AutoLoad import AutoLoad
from utils.ThreadPool import ThreadPool
from utils.LoggerHelp import logger

__author__ = "lightless"
__email__ = "root@lightless.me"

reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == "__main__":
    # 加载爬虫插件
    al = AutoLoad()
    # 如果没有参数，加载全部插件
    al.load()
    # 如果想加载指定插件，可采用下面的写法
    # al.load(cls=["KPSpider"])

    if not len(al.spiders):
        logger.error("No Spiders loaded, exit.")
        sys.exit(1)

    message = "Loaded spiders: "
    for s in al.spiders:
        message += str(s.__class__).split(".")[-1] + ", "
    logger.info(message)

    # 创建线程池
    tp = ThreadPool()
    for sp in al.spiders:
        # 将spider中的run方法添加到线程池中
        tp.add_function(sp.run)

    # 开始爬取代理部分
    tp.run()

    logger.info("All done. Writing files...")
    # 解析结果，并写入文件
    with open("proxy-ip-list.csv", "w") as ff:

        # 写入BOM头
        ff.write(codecs.BOM_UTF8)
        # TODO: fix get value from dict
        while not al.results.empty():
            res = al.results.get_nowait()
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
