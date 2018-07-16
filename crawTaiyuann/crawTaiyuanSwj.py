#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/3 下午5:21
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取太原市商务局文件
# @File    : crawTaiyuan.py
# @Software: PyCharm

from lxml import etree
import crawTaiyuanGtj
import os
import time

class CrawTaiyuanSwj(crawTaiyuanGtj.CrawTaiyuanGtj):

    def __init__(self):
        super(CrawTaiyuanSwj, self).__init__()

    def firstPageT(self, c):
        '''
        http://sswj.taiyuan.gov.cn/zfxxgk/xxgkml/zcfg/index.shtml#, 获得该页面的'文件页面'链接
        :param c: 网页源码
        :return:
        '''
        sel = etree.HTML(c)
        l = sel.xpath('//tbody/tr/td[@class="sp1"]//a/@href')
        l = list(map(lambda x:'http://sswj.taiyuan.gov.cn/'+x, l))
        print(l)
        return l

if __name__ == '__main__':
    firstUri = 'http://sswj.taiyuan.gov.cn/zfxxgk/xxgkml/zcfg/index.shtml'
    t = CrawTaiyuanSwj()
    # t.firstPage(firstUri, 3)
    # t.next()
    # t.getUsefulInfo(pageInfo)
    t.run(firstUri, '太原/商务局', 3)
