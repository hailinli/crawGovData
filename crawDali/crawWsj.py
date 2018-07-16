#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/25 下午10:17
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取大理市政府网站文件
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
        l = list(map(lambda x:'http://www.dlwsj.gov.cn/'+x, l))
        # print(l)
        return l, sel

    def hasNextPage(self, html):
        '''
        内容是否有下一页http://www.dlwsj.gov.cn/zfxxgk/index_4.html
        :param html:
        :return:
        '''
        c = html.xpath('string(//div[@class="list-page padding-5"])')
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
            url = urlBase.replace('index.html', 'index_%s.html'%i)
        print(len(r))
        return r


    def getText(self, item):
        '''
        提取c[0]
        :param item:
        :return:
        '''
        if isinstance(item, str):
            return ''
        t = item.xpath('text()')
        if len(t) > 0:
            return t[0]
        return ''

    def getUsefulInfo(self, url):
        '''
        访问url,并下载网页,并解析得到需要的文件
        http://www.yndali.gov.cn/index.php?m=content&c=index&a=show&catid=82&id=17577
        :param url:
        :return:
        '''
        c = self.get(url)
        html = etree.HTML(c)
        xxmc = self.xpath_text(html, '//div[@id="text-t"]/h4')  # 信息名称
        xg = html.xpath('//div[@class="panel-940"]/span')  # 相关
        ly, zz, fbrq, _ = xg[:4]+ ['']*(4-len(xg))
        ly = self.getText(ly)
        zz = self.getText(zz)
        fbrq = self.getText(fbrq)
        nr = self.getContent(html, '//div[@class="panel-940" and @id="text-s"]')
        tplj = html.xpath('//div[@class="main grid-1260"]//p//a/@href')
        print(xxmc)
        print(ly, zz, fbrq)
        print(nr)
        print(tplj)
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
        if len(tplj) > 0:
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
        urls = self.getPages(url)
        print(urls)
        for url in urls:
            xxmc, ly, zz, fbrq, nr, tplj = self.getUsefulInfo(url)
            self.writeUsefulInfo(dic, url, xxmc, ly, zz, fbrq, nr, tplj)

if __name__ == '__main__':
    runUri ='http://www.dlwsj.gov.cn/zfxxgk/index.html'
    firstUri = 'http://www.dlwsj.gov.cn/zfxxgk/index_5.html'
    pageInfo = 'http://www.dlwsj.gov.cn/zfxxgk/2017-02-04/196.html'
    pageInfo = 'http://www.dlwsj.gov.cn/zfxxgk/2017-02-09/207.html'
    t = CrawDlWsj()
    # t.firstPage(firstUri)
    # t.getPages(runUri)
    # t.getUsefulInfo(pageInfo)
    t.run(runUri, '大理/卫计委')  # 市政府文件