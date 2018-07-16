#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/25 下午10:17
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取大理财政局网站文件
# @File    : crawWsj.py
# @Software: PyCharm
from lxml import etree
import crawWsj
import os


class CrawDlf(crawWsj.CrawDlWsj):

    def __init__(self):
        super(CrawDlf, self).__init__()

    def firstPage(self, url):
        '''
        http://www.dlwsj.gov.cn/zfxxgk/index_5.html, 获得该页面的'文件'链接
        :param url:
        :return:
        '''
        c = self.get(url)  # 网页内容
        sel = etree.HTML(c)
        l = sel.xpath('//ul[@class="list panel-ul padding-10"]//li/a/@href')
        def isHttp(s):
            if 'http' in s:
                return False
            return True
        l = list(filter(isHttp, l))
        l = list(map(lambda x:'http://www.dlf.gov.cn/'+x, l))
        # print(l)
        return l, sel

    def hasNextPage(self, html):
        '''
        内容是否有下一页http://www.dlwsj.gov.cn/zfxxgk/index_4.html
        :param html:
        :return:
        '''
        c = html.xpath('string(//ul[@class="list-page padding-5"])')
        # print(c)
        if '下一页' in c:
            return True
        else:
            return False

    def getPages(self, urlBase):
        '''
        http://www.dlwsj.gov.cn/zfxxgk/index.html
        :param url:
        :return:
        '''
        i = 1
        url = urlBase
        r = []
        while True:
            t, html = self.firstPage(url)
            r += t
            if not self.hasNextPage(html):
                break
            i += 1
            url = urlBase.replace('PageNo=1', 'PageNo=%s'%i)
        # print(len(r))
        # print(r)
        return r

if __name__ == '__main__':
    firstUri = 'http://www.dlf.gov.cn/plus/list.php?tid=3&TotalResult=573&PageNo=1'
    pageInfo = 'http://www.dlf.gov.cn/a/xinxigongkai/20180311/2592.html'
    t = CrawDlf()
    # print(t.firstPage(firstUri))
    # t.getPages(firstUri)
    # t.getUsefulInfo(pageInfo)
    t.run(firstUri, '大理/财政局')  # 市政府文件