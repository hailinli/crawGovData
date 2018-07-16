#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/25 下午10:17
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取大理自治州食药监网站文件
# @File    : crawWsj.py
# @Software: PyCharm
from lxml import etree
import crawBase
import os

class CrawDlWsj(crawBase.CrawBase):

    def __init__(self):
        super(CrawDlWsj, self).__init__()

    def firstPage(self, url):
        '''
        http://www.syj.gov.cn/list/?2_1.html, 获得该页面的'文件'链接
        :param url:
        :return:
        '''
        c = self.get(url)  # 网页内容
        sel = etree.HTML(c)
        l = sel.xpath('//div[@class="newslist f14"]//li/a/@href')
        def isHttp(s):
            if 'http' in s:
                return False
            return True
        l = list(filter(isHttp, l))
        l = list(map(lambda x:'http://www.syj.gov.cn/'+x, l))
        # print(l)
        return l

    def getPages(self):
        '''
        http://www.syj.gov.cn/list/?2_1.html
        :param url:
        :return:
        '''
        r1 = ['http://www.syj.gov.cn/list/?2_1.html','http://www.syj.gov.cn/list/?2_2.html', 'http://www.syj.gov.cn/list/?2_3.html']
        r2 = []
        for i in r1:
            r2 += self.firstPage(i)
        return r2


    def getText(self, xg):
        '''
        提取c[0]
        :param item:
        :return:
        '''
        if len(xg) >0:
            xg = xg[0]
        else:
            return '',''
        t = xg.split('日期：')
        rq = t[1].strip()
        ly = t[0].split('来源：')[1].strip()
        return rq,ly

    def getUsefulInfo(self, url):
        '''
        访问url,并下载网页,并解析得到需要的文件
        http://www.syj.gov.cn/content/?243.html
        :param url:
        :return:
        '''
        c = self.get(url)
        html = etree.HTML(c)
        xxmc = self.xpath_text(html, '//div[@class="news"]/h2')  # 信息名称
        xg = html.xpath('//div[@class="news"]/div/text()')  # 相关
        fbrq,ly  = self.getText(xg)
        zz = ''
        tplj = []
        nr = self.getContent(html, '//div[@class="news"]/div[@class="info"]')
        # tplj = html.xpath('//div[@class="main grid-1260"]//p//a/@href')
        # print(xxmc)
        # print(xg)
        # print(ly, zz, fbrq)
        # print(nr)
        # print(tplj)
        return xxmc, ly, zz, fbrq, nr, tplj

    def writeUsefulInfo(self, dic, url, xxmc, ly, zz, fbrq, nr, tplj):
        '''
        写数据到文本文件
        :param wz: str, 位置(分类)
        :param url: str, 网页链接
        :param xxmc: str, 信息名称
        :param fbrq: str, 发布日期
        :param zz: str, 发布部门
        :param ly: str, 发布部门
        :param nr: 内容
        :return:
        '''
        xxmc = xxmc.replace('/','').replace(' ','')
        fname = '%s/%s.txt' %(dic, xxmc)
        fbbm = zz if zz != '' else ly
        with open(fname, 'w') as f:
            f.write('网页地址: %s\n' %url)
            f.write('索引号:    \n')
            f.write('信息分类:    \n')
            f.write('发布机构: %s\n' %fbbm)
            f.write('生成日期: %s\n' % fbrq)
            f.write('生效日期:    \n')
            f.write('废止日期:    \n')
            f.write('信息名称: %s\n' % xxmc)
            f.write('文   号:    \n')
            f.write('关键词:    \n\n')
            f.write('内容:%s\n%s\n' % (nr, '\n'.join(tplj)))
        picPath = '%s/%s' %(dic, xxmc)
        # print(picPath)
        os.system('mkdir -p %s' %picPath)
        for u in tplj:
            n = u[-10:]
            self._secureCrawFile(u, {}, '%s/%s'%(picPath, n))

    def run(self, url, dic):
        '''
        进入 first pase 开始爬取文章
        :param url:
        :param dic:
        :return:
        '''
        os.system('mkdir -p %s' % dic)  # 创建文件夹
        urls = self.getPages()
        print(urls)
        for url in urls:
            xxmc, ly, zz, fbrq, nr, tplj = self.getUsefulInfo(url)
            self.writeUsefulInfo(dic, url, xxmc, ly, zz, fbrq, nr, tplj)

if __name__ == '__main__':
    firstUri = 'http://www.syj.gov.cn/list/?2_1.html'
    pageInfo = 'http://www.syj.gov.cn/content/?2065.html'
    t = CrawDlWsj()
    # t.firstPage(firstUri)
    # print(t.getPages())
    # t.getUsefulInfo(pageInfo)
    t.run(firstUri, '大理/食药监')  # 市政府文件