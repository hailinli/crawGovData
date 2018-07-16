#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/3 下午5:21
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取太原市国土资源局网站文件
# @File    : crawTaiyuan.py
# @Software: PyCharm

from lxml import etree
import crawTaiyuanFgw
import os
import time

class CrawTaiyuanGtj(crawTaiyuanFgw.CrawTaiyuanFgw):

    def __init__(self):
        super(CrawTaiyuanGtj, self).__init__()

    def firstPageT(self, c):
        '''
        http://gtj.taiyuan.gov.cn/xxgkml/index.shtml#, 获得该页面的'文件页面'链接
        :param c: 网页源码
        :return:
        '''

        sel = etree.HTML(c)
        l = sel.xpath('//tbody/tr/td[@class="sp1"]//a/@href')
        l = list(map(lambda x:'http://gtj.taiyuan.gov.cn/'+x, l))
        print(l)
        return l

    def getUsefulInfo(self, url):
        '''
        访问url,并下载网页,并解析得到需要的信息
        http://www.taiyuan.gov.cn/doc/2017/12/29/183470.shtml
        :param url:
        :ret
        '''
        xxmc, syh, fbsj, fbly, wh, fl, nr, tplj = super(CrawTaiyuanGtj, self).getUsefulInfo(url)
        if nr == '':
            nr = self.getContent(self.useInfo, '//div[@id="zoom"]')
        if tplj == '':
            tplj = self.useInfo.xpath('//div[@id="zoom"]//a/@href')
        return xxmc, syh, fbsj, fbly, wh, fl, nr, tplj

if __name__ == '__main__':
    firstUri = 'http://gtj.taiyuan.gov.cn/xxgkml/zcfg/index.shtml'
    pageInfo = 'http://gtj.taiyuan.gov.cn/doc/2018/05/15/498567.shtml'
    t = CrawTaiyuanGtj()
    # t.firstPage(firstUri, 79)
    # t.next()
    # t.getUsefulInfo(pageInfo)
    t.run(firstUri, '太原/国土资源局', 16)
