#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/16 下午16:41
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取大庆政府网站文件
# @File    : crawDaqingGov.py
# @Software: PyCharm
from lxml import etree
import crawBase
import os
import re

class CrawDaqingGov(crawBase.CrawBase):

    def __init__(self):
        super(CrawDaqingGov, self).__init__()

    def firstHasNextPage(self, url):
        '''
        爬取网页(如链接为http://www.daqing.gov.cn/zfgw/szfwj/index_2.shtml)中的文件链接,判断是否有下一页
        :param url:
        :return: int, 页面数
        '''
        firstPageCnt = self.get(url)
        # print(firstPageCnt)
        sel = etree.HTML(firstPageCnt)
        pageCnt = sel.xpath('//div[@class="middle_list_Content_pages"]/a/text()')  # 定位
        pageCntText = ''.join(pageCnt)
        if '后一页' in pageCntText:
            # print(pageCntText)
            # print("True")
            return True
        # print('False')
        return False

    def firstGenPageUrl(self, url, num):
        '''
        http://www.daqing.gov.cn/zfgw/szfwj/index_2.shtml
        根据number,拼接出urls
        :param num:
        :return: r, url
        '''
        baseUri = '/'.join(url.split('/')[:-1])
        r = 'index_%s.shtml' % num
        url = baseUri + '/' + r
        # print(url)
        return url

    def firstPage(self, url):
        '''
        爬取网页(如链接为http://www.daqing.gov.cn/zfgw/szfwj/index_2.shtml)中的市政府文件的链接
        :return: list, 列表元素为url字符串
        '''
        firstPageCnt = self.get(url)
        sel = etree.HTML(firstPageCnt)
        urls = sel.xpath('//div[@class="middle_list_Content"]/ul/li/a/@href')
        urls = list(map(lambda x: 'http://www.daqing.gov.cn/'+x if 'http' not in x else '', urls))
        # print(len(urls))
        # print(urls)
        # print(self.get(urls[0]))
        return urls


    def get_xinxi_dic(self, line):
        """
        从标题里解析部门
        :param st:
        :return:
        """
        RE_RE = ['\[(.*)\]', '\【(.*)\】']
        for re_RE in RE_RE:
            m = re.compile(re_RE)
            gs = m.findall(line)
            for g in gs:
                print(g)
                return g

    def getUsefulInfo(self, url):
        '''
        访问url,并下载网页,并解析得到需要的文件
        :param url:
        :return:
        '''
        c = self.get(url)
        html = etree.HTML(c)
        pos = html.xpath('//div[@class="middle_list_Breadcrumb"]/*')  # 现在位置
        pos = list(map(lambda x:x.text, pos))
        r = '/'.join(pos)  # 位置
        xxmc = self.xpath_text(html, '//div[@class="middle_Content_Title"]')  # 信息名称
        fbrq = self.xpath_text(html, '//div[@class="middle_Content_Other_Time"]')  # 发布日期
        fbrq = self.split(fbrq, 1, '：')
        wh = self.xpath_text(html, '//div[@class="middle_Content_SubTitle"]')  # 文号
        nr = self.getContent(html, '//div[@class="middle_Content_Content"]')
        # fbbm = self.xpath_text(html, '//div[@class="middle_Content_Other_From"]')
        # fbbm = self.split(fbbm, 1, '：')
        ### print(url)
        ##################
        fbbm = str(self.get_xinxi_dic(xxmc)).strip()
        ##################

        # print(r)
        # print(xxmc)
        # print(fbrq)
        # print(wh)
        # print(nr)
        return url, r, xxmc, fbrq, wh, nr, fbbm

    def writeUsefulInfo(self, dic, url, wz, xxmc, fbrq, fbbm, wh, nr):
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
        xxmc = xxmc.replace('/','')
        if not os.path.exists(dic):
            os.makedirs(dic)
            # print(dir)
            # os.system('mkdir -p %s' % dic)
        fname = '%s/%s.txt' %(dic, xxmc)
        with open(fname, 'w') as f:
            f.write('网页地址: %s\n' %url)
            f.write('索引号:    \n')
            f.write('信息分类: %s\n' % wz)
            f.write('发布机构: %s\n' % fbbm)
            f.write('生成日期: %s\n' % fbrq)
            f.write('生效日期:    \n')
            f.write('废止日期:    \n')
            f.write('信息名称: %s\n' % xxmc)
            f.write('文   号: %s\n' % wh)
            f.write('关键词:    \n\n')
            f.write(nr)  # 写内容

    def run(self, url, dic, fbbm=''):
        '''
        进入 first pase 开始爬取文章
        :param url:
        :param dic:
        :param fbbm: 传入发布部门
        :return:
        '''
        os.system('mkdir -p %s' % dic)
        i = 2
        while True:
            secUrls = self.firstPage(url)
            # print(secUrls)
            # print(len(secUrls))
            for secUrl in secUrls:
                if '' == secUrl:
                    continue
                thirdUrl, r, xxmc, fbrq, wh, nr, fbbm1 = self.getUsefulInfo(secUrl)
                fbbm_raw = fbbm
                if fbbm == '':
                    fbbm = fbbm1
                    dic = '%s/%s' %('/'.join(dic.split('/')[:-1]), fbbm)
                self.writeUsefulInfo(dic, thirdUrl, r, xxmc, fbrq, fbbm, wh, nr)
                fbbm = fbbm_raw
                # break
            if self.firstHasNextPage(url):
                url = self.firstGenPageUrl(url, i)
                i += 1
                # print(url)
            else:
                break

if __name__ == '__main__':
    firstUri = 'http://www.daqing.gov.cn/zfgw/szfwj/index_2.shtml'
    infoUri = 'http://www.daqing.gov.cn/zfgw/szfwj/548548.shtml'
    t = CrawDaqingGov()
    # print(t.get('http://www.daqing.gov.cn/zfgw/szfwj/index_2.shtml'))
    # t.firstGenPageUrl(firstUri, 4)
    # t.firstPage(firstUri)
    # t.getUsefulInfo(infoUri)

    # url = 'http://www.daqing.gov.cn/zfgw/szfwj/'
    # t.run(url, 'data/大庆/市政府文件', '大庆市人民政府')  # 市政府文件
    # url = 'http://www.daqing.gov.cn/zfgw/szfbwj/'
    # t.run(url, 'data/大庆/市政府办文件', '大庆市人民政府办公室')  # 市政府办文件
    url = 'http://www.daqing.gov.cn/xxgk/bmxxml/index.shtml'
    t.run(url, 'data/大庆/部门文件')  # 部门文件