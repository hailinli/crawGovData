#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/3 下午5:21
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取太原市政府网站文件
# @File    : crawTaiyuan.py
# @Software: PyCharm

from lxml import etree
import crawBase
import os
import time

class CrawTaiyuan(crawBase.CrawBase):

    def __init__(self):
        super(CrawTaiyuan, self).__init__()

    def next(self):
        '''
        得到下一页网页
        :param ith: 总共的页数
        :return:
        '''
        xyy = self.driver.find_element_by_xpath('//div[@id="fenye"]/p/a[last()-1]')  # 找到下一页
        print(xyy.text)
        xyy.click()
        time.sleep(2)
        return self.driver.page_source

    def firstPageT(self, c):
        '''
        http://www.taiyuan.gov.cn/zfxxgk/szfxxgkml/fgwjjjd/szfwj/index.shtml, 获得该页面的'文件页面'链接
        :param c: 网页源码
        :return:
        '''

        sel = etree.HTML(c)
        l = sel.xpath('//tbody/tr/td[@class="sp1"]//a/@href')
        l = list(map(lambda x:'http://www.taiyuan.gov.cn/'+x, l))
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
        self.startPhantomJS()
        c = self.getFromSelenium(url) # 网页内容
        r += self.firstPageT(c)
        i = 1
        while i < ith:
            i += 1
            t = self.next()
            if t == '':
                break
            # print(t)
            r += self.firstPageT(t)
        self.stopPhantomJS()
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
        xxmc = self.xpath_text(html, '//div[@class="pd20 news_con"]/h3')  # 信息名称
        # print(xxmc)
        syh = self.xpath_text(html, '//tbody/tr[1]/td[2]')
        # print(syh)
        fbsj = self.xpath_text(html, '//tbody/tr[1]/td[4]')
        # print(fbsj)
        fbly = self.xpath_text(html, '//tbody/tr[2]/td[2]')
        # print(fbly)
        wh = self.xpath_text(html, '//tbody/tr[2]/td[4]')
        # print(wh)
        gjc = self.xpath_text(html, '//tbody/tr[3]/td[2]')
        # print(gjc)
        nr = self.getContent(html, '//div[@id="zoom"]/p')
        # print(nr)
        tplj = {}
        return xxmc, syh, fbsj, fbly, wh, gjc, nr, tplj

    def writeUsefulInfo(self, dic, url, xxmc, syh, fbsj, fbly, wh, gjc, nr, tplj):
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
            f.write('索引号: %s\n' %syh)
            f.write('信息分类:    \n')
            f.write('发布机构: %s\n' %fbly)
            f.write('生成日期: %s\n' % fbsj)
            f.write('生效日期:    \n')
            f.write('废止日期:    \n')
            f.write('信息名称: %s\n' % xxmc)
            f.write('文   号: %s\n' %wh)
            f.write('关键词: %s\n\n' %gjc)
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
            xxmc, syh, fbsj, fbly, wh, gjc, nr, tplj = self.getUsefulInfo(f)
            self.writeUsefulInfo(dic, f, xxmc, syh, fbsj, fbly, wh, gjc, nr, tplj)

if __name__ == '__main__':
    firstUri = 'http://www.taiyuan.gov.cn/zfxxgk/szfxxgkml/fgwjjjd/szfwj/index.shtml'
    pageInfo = 'http://www.taiyuan.gov.cn/doc/2018/04/03/268644.shtml'
    t = CrawTaiyuan()
    # t.firstPage(firstUri, 79)
    # t.next()
    # t.getUsefulInfo(pageInfo)
    t.run(firstUri, '太原/市政府文件', 79)  # 市政府文件
