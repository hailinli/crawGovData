#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/21 下午14:41
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取大理白族自治州政府网站文件
# @File    : crawDlbzzzzGov.py
# @Software: PyCharm
from lxml import etree
import crawBase
import os

class CrawDlbzzzzGov(crawBase.CrawBase):

    def __init__(self):
        super(CrawDlbzzzzGov, self).__init__()

    def firstPage(self, url):
        '''
        http://www.dali.gov.cn/dlzwz/5117219474646237184/index.html, 获得该页面的'更多'下链接
        :param url:
        :return:
        '''
        c = self.get(url)  # 网页内容
        sel = etree.HTML(c)
        l = sel.xpath('//div[@class="List2-t"]/span/a/@href')
        al = list(map(lambda x:'http://www.dali.gov.cn/'+x, l))
        # print(al)
        return al

    def secondPage(self, url):
        '''
        http://www.dali.gov.cn//dlzwz/5117219530480812032/index.html, 获得该页面下的文章链接
        :param url:
        :return: list,文章链接; str,网页
        '''
        c = self.get(url)
        sel = etree.HTML(c)
        l = sel.xpath('//tr/td[@width="87%"]/a/@href')
        al = list(map(lambda x:'http://www.dali.gov.cn/'+x, l))
        # print(al)
        return al

    def secondPageHasNext(self, url):
        '''
        http://www.dali.gov.cn//dlzwz/5117219530480812032/index.html 提取包含'下一页'的链接
        :param url:
        :return:
        '''
        c = self.get(url)
        sel = etree.HTML(c)
        l = sel.xpath('//tr/td[@align="center"]/a/@href')
        if len(l) == 2:
            return 'http://www.dali.gov.cn/' + l[0]
        return ''

    def getUsefulInfo(self, url):
        '''
        访问url,并下载网页,并解析得到需要的文件
        :param url:
        :return:
        '''
        c = self.get(url)
        html = etree.HTML(c)
        l = html.xpath('//tbody/tr/td/table[@xmlns and @width]//strong/text()')[:2]  # 发布机构 信息名称
        fbbm, xxmc = l + ['']*(2-len(l))
        wh = html.xpath('//table[@xmlns and @width]//td[@align="center"]/text()')[0]  # 文号
        nr = self.getContent(html, '//tbody//tbody//td[@width="992"]//tbody')
        # print(fbbm, xxmc, wh)
        return fbbm, xxmc, wh, nr

    def writeUsefulInfo(self, dic, url, xxmc, fbbm, wh, nr):
        '''
        写数据到文本文件
        :param wz: str, 位置(分类)
        :param url: str, 网页链接
        :param xxmc: str, 信息名称dic
        :param fbrq: str, 发布日期
        :param fbbm: str, 发布部门
        :param nr: 内容
        :return:
        '''
        xxmc = xxmc.replace('/','')
        fname = '%s/%s.txt' %(dic, xxmc)
        with open(fname, 'w') as f:
            f.write('网页地址: %s\n' %url)
            f.write('索引号:    \n')
            f.write('信息分类:    \n')
            f.write('发布机构: %s\n' % fbbm)
            f.write('生成日期:    \n')
            f.write('生效日期:    \n')
            f.write('废止日期:    \n')
            f.write('信息名称: %s\n' % xxmc)
            f.write('文   号: %s\n' % wh)
            f.write('关键词:    \n\n')
            f.write(nr)  # 写内容

    def run(self, url, dic):
        '''
        进入 first pase 开始爬取文章
        :param url:
        :param dic:
        :return:
        '''
        os.system('mkdir -p %s' % dic)  # 创建文件夹
        for f in self.firstPage(url):  # '更过'链接
            while True:
                for s in self.secondPage(f):
                    fbbm, xxmc, wh, nr = self.getUsefulInfo(s)
                    self.writeUsefulInfo(dic, s, xxmc, fbbm, wh, nr)
                    # print(wh)
                # 进入下一页
                s = self.secondPageHasNext(f)
                if s == '':
                    break
                else:
                    f = s

if __name__ == '__main__':
    firstUri = 'http://www.dali.gov.cn/dlzwz/5117219474646237184/index.html'
    secondUri = 'http://www.dali.gov.cn//dlzwz/5117219530480812032/index.html'
    pageInfo = 'http://www.dali.gov.cn/dlzwz/5117220634287407104/20180621/323114.html'
    t = CrawDlbzzzzGov()
    # t.firstPage(firstUri)
    # t.secondPage(secondUri)
    # t.getUsefulInfo(pageInfo)

    t.run(firstUri, '大理/州政府文件')  # 州政府文件
    url = 'http://www.dali.gov.cn/dlzwz/5117220574157864960/index.html'
    t.run(url, '大理/州政府办文件')  # 州政府办文件