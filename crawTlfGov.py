#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/12 下午12:39
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取吐鲁番政府文件
# @File    : crawTlfGov.py
# @Software: PyCharm
from lxml import etree
import crawBase
import os

class CrawTlfGov(crawBase.CrawBase):
    def __init__(self):
        super(CrawTlfGov, self).__init__()

    def firstPageNum(self, url):
        '''
        爬取网页(如链接为http://www.tlf.gov.cn/zwgk/mlxxlb.jsp?urltype=tree.TreeTempUrl&wbtreeid=6075)中的文件链接的页数
        :param url:
        :return: int, 页面数
        '''
        # print(url)
        firstPageCnt = self.get(url)
        sel = etree.HTML(firstPageCnt)
        pageCnt = sel.xpath('//td[@nowrap and @align="left"]')[0]  # 定位
        pageText = pageCnt.xpath('string(.)')  # 提取元素text
        num = pageText.split('/')[1]  # 获得想要的text
        # print(num)
        return int(num)

    def firstPageUrls(self, url, num):
        '''
        根据number,拼接出urls
        :param num:
        :return: list, url列表
        '''
        # print(url)
        urls = []
        for i in range(1, num+1):
            t = 'a51p=%s' % i
            turl = url.replace('a51p=1', t)
            urls.append(turl)
        # print(urls)
        return urls

    def firstPage(self, url):
        '''
        爬取网页(如链接为http://www.tlf.gov.cn/zwgk/mlxxlb.jsp?urltype=tree.TreeTempUrl&wbtreeid=6084)中的文件的链接
        :return: list, 列表元素为url字符串
        '''
        firstPageCnt = self.get(url)
        sel = etree.HTML(firstPageCnt)
        urls = sel.xpath('//div[@class="c51"]//tbody/tr//a/@href')  # 提取链接
        urls = list(set(urls))  # 去重
        urls = list(map(lambda x:'http://www.tlf.gov.cn/'+x, urls))  # 链接拼接
        # print(len(urls))
        # print(urls)
        return urls

    def getUsefulInfo(self, url):
        '''
        访问url,并下载网页,并解析得到需要的文件
        :param url:
        :return:
        '''
        c = self.get(url)
        html = etree.HTML(c)
        wz = html.xpath('string(//table[@class="winstyle15882"])')
        wz = '/'.join(wz.split('>>')[1:-1])
        xxmc = html.xpath('//td[@class="titlestyle56" or @class="titlestyle234"]/text()')[0]
        xxmc = xxmc.replace('\r\n', '').strip()
        # print(xxmc)
        t = html.xpath('//td[@class="govvaluefont56"]/text()')
        if len(t) < 4:
            t = t + ['']*(4-len(t))
        else:
            t = t[:4]
        syh, _, gkrq, fbjg = t  # 索引号,公开方式,公开日期,发布机构
        # syh  = html.xpath('//td[@class="govvaluefont56"]/text()')[:4]  # 索引号,公开方式,公开日期,发布机构
        # print(syh)
        # gkrq, fbjg, nr = '', '', ''
        nr = self.__getContent(html)  # 内容
        return wz, xxmc, syh, gkrq, fbjg, nr

    def __getContent(self, html):
        '''
        解析文章内容
        :param etreeHTML:
        :return:
        '''
        # print(etree.tostring(ps[40], encoding='unicode', pretty_print=True, method = "html"))
        ps = html.xpath('//div[@id="vsb_content_2"]/p')  # 段落
        psl = []  # 段落
        for p in ps:  # 提取每段html中的文字
            l = p.xpath('string(.)')
            psl.append(l)
        return '\n'.join(psl)

    def writeUsefulInfo(self, dic, url, wz, xxmc, syh, gkrq, fbjg, nr):
        '''
        写数据到文本文件
        :param wz:
        :param xxmc:
        :param syh:
        :param gkrq:
        :param fbjg:
        :return:
        '''
        xxmc = xxmc.replace('/','')
        fname = '%s/%s.txt' %(dic,xxmc)
        with open(fname, 'w') as f:
            f.write(url + '\n')
            f.write('索引号: %s\n' % syh)
            f.write('信息分类: %s\n' % wz)
            f.write('发布机构: %s\n' % fbjg)
            f.write('生成日期: %s\n' % gkrq)
            f.write('生效日期:    \n')
            f.write('废止日期:    \n')
            f.write('信息名称: %s\n' % xxmc)
            f.write('文   号:    \n')
            f.write('关键词:    \n\n')
            f.write(nr)  # 写内容

    def run(self, url, dic):
        '''
        进入 first pase 开始爬取文章
        :param url:
        :param dic:
        :return:
        '''
        os.system('mkdir -p %s' % dic)
        num = self.firstPageNum(url)
        urls = self.firstPageUrls(url, num)
        # print(urls)
        for url in urls:
            # print(url)
            secUrls = self.firstPage(url)
            # print(secUrls)
            # print(len(secUrls))
            for secUrl in secUrls:
                if '' == secUrl:
                    continue
                wz, xxmc, syh, gkrq, fbjg, nr = self.getUsefulInfo(secUrl)
                self.writeUsefulInfo(dic, secUrl, wz, xxmc, syh, gkrq, fbjg, nr)

if __name__ == '__main__':
    crawTlfGov = CrawTlfGov()
    url = 'http://www.tlf.gov.cn/zwgk/mlxxlb.jsp?a51t=1&a51p=1&a51c=10&urltype=tree.TreeTempUrl&wbtreeid=86'
    dic = 'data/吐鲁番/'
    crawTlfGov.run(url, dic)

    # crawTlfGov.firstPage(url)
    # url = 'http://www.tlf.gov.cn/info/365/179379.htm'
    # crawTlfGov.getUsefulInfo(url)
