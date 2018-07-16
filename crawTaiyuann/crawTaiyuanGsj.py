#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/3 下午5:21
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取太原市工商局文件
# @File    : crawTaiyuan.py
# @Software: PyCharm

from lxml import etree
import crawTaiyuanGtj
import os
import time

class CrawTaiyuanGsj(crawTaiyuanGtj.CrawTaiyuanGtj):

    def __init__(self):
        super(CrawTaiyuanGsj, self).__init__()

    def firstPageT(self, c):
        '''
        http://hbj.taiyuan.gov.cn/zfxxgk/xxgkml/zcfg/index.shtml#, 获得该页面的'文件页面'链接
        :param c: 网页源码
        :return:
        '''

        sel = etree.HTML(c)
        l = sel.xpath('//tbody/tr/td[@class="sp1"]//a/@href')
        l = list(map(lambda x:'http://gsj.taiyuan.gov.cn/'+x, l))
        print(l)
        return l

if __name__ == '__main__':
    firstUri = 'http://gsj.taiyuan.gov.cn/zfxxgk/xxgkml/fgwjjjd/index.shtml'
    pageInfo = 'http://gsj.taiyuan.gov.cn/doc/2017/07/17/266699.shtml'
    t = CrawTaiyuanGsj()
    # t.firstPage(firstUri, 4)
    # t.next()
    # t.getUsefulInfo(pageInfo)
    t.run(firstUri, '太原/工商局', 4)
