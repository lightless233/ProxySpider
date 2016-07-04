#!/usr/bin/env python
# coding: utf-8
import sys

from utils.AutoLoad import AutoLoad
from utils.ThreadPool import ThreadPool
from utils.data.LoggerHelp import logger
from utils.data.WriteFile import write_file

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
    tp.run(join=False)

    # 输出结果到文件中
    write_file_tp = ThreadPool()
    write_file_tp.add_function(write_file, results_queue=al.results, thread_pool=tp)
    write_file_tp.run()
