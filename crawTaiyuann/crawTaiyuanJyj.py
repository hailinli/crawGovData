#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/3 下午5:21
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取太原市政府网站教育局文件
# @File    : crawTaiyuan.py
# @Software: PyCharm

from lxml import etree
import crawBase
import os
import time

class CrawTaiyuanJyj(crawBase.CrawBase):

    def __init__(self):
        super(CrawTaiyuanJyj, self).__init__()

    def next(self, url, ith):
        '''
        得到下一页网页
        :param ith: 总共的页数
        :return:
        '''
        # print('ffdfd'+url)
        return url.replace('index.html', 'index_%s.html' %ith)


    def firstPageT(self, url):
        '''
        http://jyj.taiyuan.gov.cn/edu/zhengcefagui/difangfagui/index_6.html, 获得该页面的'文件页面'链接
        :param url: 网页链接
        :return:
        '''
        c = self.get(url)
        sel = etree.HTML(c)
        l = sel.xpath('//div[@class="son_content"]/ul/li/a/@href')
        l = list(map(lambda x:'http://jyj.taiyuan.gov.cn/'+x, l))
        print(l)
        return l

    def firstPage(self, url, ith):
        '''
        http://www.taiyuan.gov.cn/zfxxgk/szfxxgkml/fgwjjjd/szfwj/index.shtml, 获得该页面的'文件页面'链接
        包括点击下一页
        :param url:
        :return:
        '''
        r = []
        r += self.firstPageT(url)
        i = 1
        while i < ith:
            i += 1
            t = self.next(url, i)
            r += self.firstPageT(t)
        print(len(r))
        return r

    def getUsefulInfo(self, url):
        '''
        访问url,并下载网页,并解析得到需要的信息
        http://www.taiyuan.gov.cn/doc/2017/12/29/183470.shtml
        :param url:
        :return:
        '''
        c = self.get(url)
        html = etree.HTML(c)
        xxmc = self.xpath_text(html, '//p[@class="news_content_title_p1"]')  # 信息名称
        # print(xxmc)
        fbsj = url.split('/')[-2]
        # print(fbsj)
        nr = self.getContent(html, '//div[@class="news_content_center"]/p')
        # print(nr)
        tplj = {}
        return xxmc, fbsj, nr, tplj

    def writeUsefulInfo(self, dic, url, xxmc, fbsj, nr, tplj):
        '''
        写数据到文本文件
        :param wz: str, 位置(分类)
        :param url: str, 网页链接
        :param xxmc: str, 信息名称
        :param fbrq: str, 发布日期
        :param fbbm: str, 发布部门
        :param nr: 内容
        :return:
        '''
        xxmc = xxmc.replace('/','').replace(' ','')
        fname = '%s/%s.txt' %(dic, xxmc)
        with open(fname, 'w') as f:
            f.write('网页地址: %s\n' %url)
            f.write('索引号:    \n')
            f.write('信息分类:    \n')
            f.write('发布机构: 太原市教育局\n')
            f.write('生成日期: %s\n' % fbsj)
            f.write('生效日期:    \n')
            f.write('废止日期:    \n')
            f.write('信息名称: %s\n' % xxmc)
            f.write('文   号:    \n')
            f.write('关键词: \n')
            f.write('内容:%s\n%s\n' % (nr, '\n'.join(tplj)))

        picPath = '%s/%s' %(dic, xxmc)
        print(picPath)
        if len(tplj) > 0:
            os.system('mkdir -p %s' %picPath)
        for u in tplj:
            n = u[-10:].replace('/','_').replace(' ','')
            self._secureCrawFile(u, {}, '%s/%s'%(picPath, n))

    def run(self, url, dic, ith):
        '''
        进入 first pase 开始爬取文章
        :param url:
        :param dic:
        :param ith:总页数
        :return:
        '''
        os.system('mkdir -p %s' % dic)  # 创建文件夹
        for f in self.firstPage(url, ith):
            xxmc, fbsj, nr, tplj = self.getUsefulInfo(f)
            self.writeUsefulInfo(dic, f, xxmc, fbsj, nr, tplj)

if __name__ == '__main__':
    firstUri = 'http://jyj.taiyuan.gov.cn/edu/zhengcefagui/difangfagui/index.html'
    pageInfo = 'http://jyj.taiyuan.gov.cn//edu/zhengcefagui/difangfagui/2018-06-11/10539.html'
    t = CrawTaiyuanJyj()
    # t.firstPage(firstUri, 14)
    # t.next()
    # t.getUsefulInfo(pageInfo)
    t.run(firstUri, '太原/教育局', 14)
