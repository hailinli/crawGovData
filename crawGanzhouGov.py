#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/11 下午12:51
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬取赣州政府网站文件
# @File    : crawGanzhouGov.py
# @Software: PyCharm
from lxml import etree
import crawBase
import os

class CrawGanzhouGov(crawBase.CrawBase):

    def __init__(self):
        super(CrawGanzhouGov, self).__init__()

    def firstPageNum(self, url):
        '''
        爬取网页(如链接为http://www.ganzhou.gov.cn/c100079/list_zw_wj.shtml)中的法规文件页数
        从 {createPageHTML('page_div',10, 1,'list_zw_wj','shtml',278);} 提取出总页数
        :param url:
        :return: int, 页面数
        '''
        firstPageCnt = self.get(url)
        fcntQ = firstPageCnt.split("{createPageHTML('page_div',")[1]  # 截掉前半部分
        fcntH = fcntQ.split(";}</script>")[0]  # 截掉后半部分
        pageNum = fcntH.split(',')[0]  # 拿到页数
        # print(pageNum)
        return int(pageNum)

    def firstPageUrls(self, url, num):
        '''
        根据number,拼接出urls
        :param num:
        :return: list, url列表
        '''
        # print(url)
        urls = []
        urls.append(url)  # 添加起始url
        urlBase = url.replace('.shtml', '')
        for i in range(2, num+1):
            turl = '%s_%s.shtml' % (urlBase, i)
            urls.append(turl)
        # print(urls)
        return urls

    def firstPage(self, url):
        '''
        爬取网页(如链接为http://www.ganzhou.gov.cn/c100079/list_zw_wj.shtml)中的法规文件的链接
        :return: list, 列表元素为url字符串
        '''
        firstPageCnt = self.get(url)
        sel = etree.HTML(firstPageCnt)
        urls = sel.xpath('//div[@class="bd"]/ul/li/a/@href')
        urls = list(map(lambda x: 'http://www.ganzhou.gov.cn/'+x if 'http' not in x else '', urls))
        # print(len(urls))
        # print(urls[0])
        # print(self.get(urls[0]))
        return urls

    def getUsefulInfo(self, url):
        '''
        访问url,并下载网页,并解析得到需要的文件
        :param url:
        :return:
        '''
        c = self.get(url)
        html = etree.HTML(c)
        pos = html.xpath('//div[@class="list_position"]/*')  # 现在位置
        pos = list(map(lambda x:x.text, pos))
        r = '/'.join(pos)  # 位置
        # print(url)
        wjxx = html.xpath('//div[@class="wz_content clear"]')[0]  # 文件信息
        # print(wjxx)
        xxmc = wjxx.xpath('./h2')[0].text.strip()  # 信息名称
        fbrq = wjxx.xpath('./p')[0].text  # 发布日期
        fbrq = fbrq.replace('发布日期：','')

        # print(url)
        fbbms = wjxx.xpath('./p/span')
        if len(fbbms) >=2:
            fbbm = fbbms[1].text.replace('发布部门：','')  # 发布部门
            if fbbm != None:
                fbbm = fbbm.strip()
        else:
            fbbm = ''
        nr,fj = self.__getContent(html)
        nr = nr.strip()  # 内容
        # print(xxmc)
        # print(fbrq)
        # print(fbbm)
        # print(r)
        # print(nr)
        return url, r, xxmc, fbrq, fbbm, nr, fj

    def writeUsefulInfo(self, dic, url, wz, xxmc, fbrq, fbbm, nr, fj):
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
        fname = '%s/%s.txt' %(dic,xxmc)
        with open(fname, 'w') as f:
            f.write(url + '\n')
            f.write('索引号:    \n')
            f.write('信息分类: %s\n' % wz)
            f.write('发布机构: %s\n' % fbbm)
            f.write('生成日期: %s\n' % fbrq)
            f.write('生效日期:    \n')
            f.write('废止日期:    \n')
            f.write('信息名称: %s\n' % xxmc)
            f.write('文   号:    \n')
            f.write('关键词:    \n\n')
            f.write(nr)  # 写内容

        if len(fj) > 0:
            dicFj = '%s/%s_附件' %(dic, xxmc.replace(' ', ''))
            os.system('mkdir -p %s' %dicFj)
            for fj_i in fj:  # 下载附件
                urlFileA = self.__getUrlFileA(url, fj_i)
                # print(urlFileA)
                fji = fj_i.replace('/','')[-30:]
                fname = '%s/%s' %(dicFj, fji)
                self._secureCrawFile(urlFileA, {}, fname)

    def __getUrlFileA(self, urlGenBase, urlLast):
        '''
        得到下载文件链接基础前缀,并拼接
        :param urlGenBase:
        :param urlLast:
        :return:
        '''
        base = '/'.join(urlGenBase.split('/')[:-1])  # 去掉最后一个/
        if 'http' not in urlLast:
            t = '%s/%s' %(base, urlLast)  # 下载链接
            return t
        return urlLast

    def __getContent(self, html):
        '''
        解析文章内容
        :param etreeHTML:
        :return:
        '''
        # print(etree.tostring(ps[40], encoding='unicode', pretty_print=True, method = "html"))
        ps = html.xpath('//div[@id="UCAP-CONTENT"]//p')  # 段落
        psl = []  # 段落
        fj = []
        for p in ps:  # 提取每段html中的文字
            l = p.xpath('string(.)')
            psl.append(l)
            a = p.xpath('./a/@href')
            if len(a) > 0:  # 下载附件
                fj.append(a[0])
        return '\n'.join(psl), fj

    def run(self, urlBase, url, dic):
        '''
        进入 first pase 开始爬取文章
        :param urlBase:
        :param url:
        :return:
        '''
        os.system('mkdir -p %s' % dic)
        num = self.firstPageNum(url)
        urls = self.firstPageUrls(url, num)
        for url in urls:
            # print(url)
            secUrls = self.firstPage(url)
            # print(secUrls)
            # print(len(secUrls))
            for secUrl in secUrls:
                if '' == secUrl:
                    continue
                url, wz, xxmc, fbrq, fbbm, nr, fj = self.getUsefulInfo(secUrl)
                self.writeUsefulInfo(dic, url, wz, xxmc, fbrq, fbbm, nr, fj)
            # break

if __name__ == '__main__':
    t = CrawGanzhouGov()
    # t.firstPageNum('http://www.ganzhou.gov.cn/c100079/list_zw_wj.shtml')
    # t.firstPageUrls('http://www.ganzhou.gov.cn/c100079/list_zw_wj.shtml', 10)
    # t.firstPage('http://www.ganzhou.gov.cn/c100079/list_zw_wj.shtml')
    # t.getUsefulInfo('http://www.ganzhou.gov.cn/c100082/2018-06/01/content_9a3fcb97914a465b8a622f9a0d044563.shtml')

    urlBase = 'http://www.ganzhou.gov.cn/'
    url = 'http://www.ganzhou.gov.cn/c100079/list_zw_wj.shtml'
    t.run(urlBase, url, 'data/赣州/地方法规')
    url = 'http://www.ganzhou.gov.cn/c100080/list_zw_wj.shtml'
    t.run(urlBase, url, 'data/赣州/政府规章')
    url = 'http://www.ganzhou.gov.cn/c100081/list_zw_wj.shtml'
    t.run(urlBase, url, 'data/赣州/市府文件')
    url = 'http://www.ganzhou.gov.cn/c100082/list_zw_wj.shtml'
    t.run(urlBase, url, 'data/赣州/部门文件')
    url = 'http://www.ganzhou.gov.cn/c100083/list_zw_wj.shtml'
    t.run(urlBase, url, 'data/赣州/县市区文件')



#     l = '''
# <html>
#  <head>
#   <base href='http://example.com/' />
#   <title>Example website</title>
#  </head>
#  <body>
#   <div id='images'>
#    <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
#    <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
#    <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
#    <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
#    <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
#   </div>
#  </body>
# </html>
#         '''
#     ll = etree.HTML(l)
#     print(ll.xpath('./body')[0].xpath('./div    /a/text()'))