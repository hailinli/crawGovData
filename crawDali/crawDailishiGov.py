#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/21 下午14:41
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取大理市政府网站文件
# @File    : crawDlbzzzzGov.py
# @Software: PyCharm
from lxml import etree
import crawBase
import os

class CrawDlGov(crawBase.CrawBase):

    def __init__(self):
        super(CrawDlGov, self).__init__()

    def firstPage(self, url):
        '''
        http://www.yndali.gov.cn/index.php?m=content&c=index&a=lists&catid=481, 获得该页面的'文件'链接
        :param url:
        :return:
        '''
        c = self.get(url)  # 网页内容
        sel = etree.HTML(c)
        l = sel.xpath('//div[@class="list-cont"]//li/a/@href')
        # print(l)
        return l

    def hasNextPage(self, html):
        '''
        内容是否有下一页http://www.yndali.gov.cn/index.php?m=content&c=index&a=show&catid=82&id=17577&page=6
        :param html:
        :return:
        '''
        c = html.xpath('string(//div[@id="page"])')
        if '下一页' in c:
            return True
        else:
            return False

    def getContentPage(self, url):
        '''
        http://www.yndali.gov.cn/index.php?m=content&c=index&a=show&catid=82&id=17577,获得内容
        :param html:
        :param rule:
        :return:
        '''
        i = 1  # 内容页
        base = url
        r = ''  # 返回内容
        while True:
            # print(url)
            c = self.get(url)
            html = etree.HTML(c)
            t = self.getContent(html, '//div[@class="content clearfix"]/p')
            r += t
            if self.hasNextPage(html) == False:
                break
            i += 1
            url = base + '&page=%s' % i
        # print('www'+r)
        return r

    def getUsefulInfo(self, url):
        '''
        访问url,并下载网页,并解析得到需要的文件
        http://www.yndali.gov.cn/index.php?m=content&c=index&a=show&catid=82&id=17577
        :param url:
        :return:
        '''
        c = self.get(url)
        html = etree.HTML(c)
        xxmc = self.xpath_text(html, '//div[@class="content clearfix"]/h3')  # 信息名称
        fbsj = self.xpath_text(html, '//div[@class="desc"]')
        tplj = html.xpath('//div[@class="content clearfix"]//p/img/@src')
        tplj += html.xpath('//div[@class="content clearfix"]//p/a/@href')
        nr = self.getContentPage(url)
        # print(xxmc, fbsj)
        # print(tplj)
        # print(nr)
        return xxmc, fbsj, tplj, nr

    def writeUsefulInfo(self, dic, url, xxmc, fbrq, nr, tplj):
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
            f.write('发布机构: 大理市人民政府办公室')
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
        urls = [url, url+'&page=2']
        # print(urls)
        for url in urls:
            for f in self.firstPage(url):
                xxmc, fbsj, tplj, nr = self.getUsefulInfo(f)
                self.writeUsefulInfo(dic, f, xxmc, fbsj, nr, tplj)

if __name__ == '__main__':
    firstUri = 'http://www.yndali.gov.cn/index.php?m=content&c=index&a=lists&catid=481' # &page=2
    pageInfo = 'http://www.yndali.gov.cn/index.php?m=content&c=index&a=show&catid=483&id=13957'
    pageInfo = 'http://www.yndali.gov.cn/index.php?m=content&c=index&a=show&catid=481&id=18229'
    t = CrawDlGov()
    # t.firstPage(firstUri)
    # t.getUsefulInfo(pageInfo)

    # t.run(firstUri, '大理/市政府文件')  # 市政府文件
    url = 'http://www.yndali.gov.cn/index.php?m=content&c=index&a=lists&catid=483'
    t.run(url, '大理/市政府办文件')  # 市政府办文件