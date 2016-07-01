#!/usr/bin/env python
# coding: utf-8
import codecs
import sys

from utils.AutoLoad import AutoLoad
from utils.ThreadPool import ThreadPool

__author__ = "lightless"
__email__ = "root@lightless.me"

reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == "__main__":
    # 加载爬虫插件
    al = AutoLoad()
    al.load()

    print "Loaded spider: ",
    for s in al.spiders:
        print str(s.__class__).split(".")[-1],
    print ""

    if not len(al.spiders):
        print "No Spiders loaded, exit."
        sys.exit(1)

    # 创建线程池
    tp = ThreadPool()
    for sp in al.spiders:
        # 将spider中的run方法添加到线程池中
        tp.add_function(sp.run)

    # 开始爬取代理部分
    tp.run()

    print "All done. Writing files..."
    # 解析结果，并写入文件
    with open("proxy-ip-list.csv", "w") as ff:

        # 写入BOM头
        ff.write(codecs.BOM_UTF8)

        while not al.results.empty():
            res = al.results.get_nowait()
            ff.writelines(res[0]['url'] + "\n")
            ff.writelines("ip,port,type,protocol,location,time(s)\n")
            print "[*] url:", res[0]['url']
            res = res[1]
            for r in res:
                line = r['ip'] + "," + r['port'] + "," + r['type'] + "," + r['protocol'] + ","\
                       + r['location'] + "," + r['time']
                print "[*]", line
                ff.writelines((line+"\n").encode("utf8"))
