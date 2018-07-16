#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/3 下午5:21
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取太原市发改委网站文件
# @File    : crawTaiyuan.py
# @Software: PyCharm

from lxml import etree
import crawTaiyuan
import os
import time

class CrawTaiyuanFgw(crawTaiyuan.CrawTaiyuan):

    def __init__(self):
        super(CrawTaiyuanFgw, self).__init__()

    def next(self):
        '''
        得到下一页网页
        :param ith: 总共的页数
        :return:
        '''
        xyy = self.driver.find_element_by_xpath('//div[@id="pages"]/span[last()-3]/a')  # 找到下一页
        print(xyy.text)
        xyy.click()
        time.sleep(2)
        return self.driver.page_source

    def firstPageT(self, c):
        '''
        http://gtj.taiyuan.gov.cn/xxgkml/index.shtml#, 获得该页面的'文件页面'链接
        :param c: 网页源码
        :return:
        '''

        sel = etree.HTML(c)
        l = sel.xpath('//tbody/tr/td[@class="sp1"]//a/@href')
        l = list(map(lambda x:'http://fgw.taiyuan.gov.cn/'+x, l))
        print(l)
        return l

    def getUsefulInfo(self, url):
        '''
        访问url,并下载网页,并解析得到需要的信息
        http://www.taiyuan.gov.cn/doc/2017/12/29/183470.shtml
        :param url:
        :return:
        '''
        c = self.get(url)
        html = etree.HTML(c)
        xxmc = self.xpath_text(html, '//div[@class="mainCont"]/h1')  # 信息名称
        print(xxmc)
        syh = self.xpath_text(html, '//tbody/tr[1]/td[2]')
        # print(syh)
        fl = self.xpath_text(html, '//tbody/tr[1]/td[4]')
        # print(fl)  # 分类
        fbsj = self.xpath_text(html, '//tbody/tr[1]/td[6]')
        # print(fbsj)
        fbly = self.xpath_text(html, '//tbody/tr[2]/td[2]')
        # print(fbly)
        wh = self.xpath_text(html, '//tbody/tr[2]/td[4]')
        # print(wh)
        nr = self.getContent(html, '//div[@id="Zoom" or @id="zoom"]/p')
        # print(nr)
        tplj = html.xpath('//div[@id="zoom" or @id="Zoom"]/p//a/@href')
        tplj = list(map(lambda x:'http://fgw.taiyuan.gov.cn/'+x, tplj))
        tplj = list(set(tplj))
        # print(tplj)
        self.useInfo = html
        return xxmc, syh, fbsj, fbly, wh, fl, nr, tplj

    def writeUsefulInfo(self, dic, url, xxmc, syh, fbsj, fbly, wh, fl, nr, tplj):
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
            f.write('信息分类: %s\n' %fl)
            f.write('发布机构: %s\n' %fbly)
            f.write('生成日期: %s\n' % fbsj)
            f.write('生效日期:    \n')
            f.write('废止日期:    \n')
            f.write('信息名称: %s\n' % xxmc)
            f.write('文   号: %s\n' %wh)
            f.write('关键词: \n\n')
            f.write('内容:%s\n%s\n' % (nr, '\n'.join(tplj)))

        picPath = '%s/%s' %(dic, xxmc)
        print(picPath)
        if len(tplj) > 0:
            os.system('mkdir -p %s' %picPath)
        for u in tplj:
            n = u[-10:].replace('/','_').replace(' ','')
            self._secureCrawFile(u, {}, '%s/%s'%(picPath, n))

if __name__ == '__main__':
    firstUri = 'http://fgw.taiyuan.gov.cn/zfxxgk/xxgkml/fgwjjjd/index.shtml'
    pageInfo = 'http://fgw.taiyuan.gov.cn//doc/2017/11/08/588354.shtml'
    t = CrawTaiyuanFgw()
    # t.firstPage(firstUri, 79)
    # t.next()
    # t.getUsefulInfo(pageInfo)
    t.run(firstUri, '太原/发改委', 37)  # 市政府文件
