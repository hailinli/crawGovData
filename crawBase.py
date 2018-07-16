#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/11 下午1:04
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 爬虫基类
# @File    : crawBase.py
# @Software: PyCharm

import random
import requests
from selenium import webdriver
import time
import log
import logging
log.initLogConf()
logg = logging.getLogger(__file__)



class CrawBase:
    '''
    爬虫基类
    '''
    def __init__(self):
        '''
        self.baseHeaders可以在继承类里面设置
        '''
        self.user = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
        ]
        self.baseHeaders = {'User-Agent': random.choice(self.user)}  # 更新头

    def get(self, url, total=3, encode=''):
        '''
        安全的访问网页链接
        :param url:
        :param headers:
        :return:
        '''
        try:
            r = requests.get(url, headers=self.baseHeaders, timeout=5)
        except Exception as e:
            logg.warn(e)
            if total>0:
                time.sleep(5)
                return self.get(url, total-1)
            return False
        logg.info('爬取成功: url, %s' %url)
        # 获取网页编码
        encodings = requests.utils.get_encodings_from_content(r.text)
        # print(encodings)
        if len(encodings) == 0:
            encoding = 'gbk'
        else:
            encoding = encodings[0]
        # try:
        #     re = r.content.decode(encoding)
        # except Exception as e:
        #     return ''
        print(url)
        r.encoding = encoding
        return r.text
        # return r.content.decode(encoding)

    def startPhantomJS(self):
        '''
        启动phantomjs
        :return:
        '''
        self.driver = webdriver.PhantomJS()

    def getFromSelenium(self, url):
        '''
        从浏览器中获得网页源码
        :param url:
        :return:
        '''
        self.driver.get(url)
        time.sleep(2)
        str_html = self.driver.page_source
        return str_html

    def stopPhantomJS(self):
        '''
        停止phantomjs
        :return:
        '''
        self.driver.close()

    def _crawlFile(self, pngUri, params, fileName):
        '''
        下载文件
        :param pngUri:
        :param fileName:
        :return:
        '''
        r = requests.get(pngUri, params=params, headers=self.baseHeaders)
        with open(fileName, 'wb') as code:
            code.write(r.content)

    def _secureCrawFile(self, pngUri, params, fileName, total=3):
        '''
        安全的下载图片,4次下载都失败,那么返回错误
        :param pngUri:
        :param fileName:
        :param total:
        :return:
        '''
        # print(pngUri)
        # print(fileName)
        print(pngUri)
        try:
            self._crawlFile(pngUri, params, fileName)
        except Exception as e:
            logg.warn(e)
            if total>0:
                return self._secureCrawFile(pngUri, params, fileName, total-1)
            return False
        return True

    def xpath_text(self, item, rule, tail = False):
        '''
        获取通过rule解析出的item列表,获取第一个item并获得其text
        :param item: xpath item, html
        :param rule:
        :param tail:
        :return:
        '''
        list = item.xpath(rule)
        # print(list)
        if len(list):
            if (tail):
                return list[0].tail
            else:
                r = list[0].text
                # r = list[0].xpath('text()')
                if r != None:
                    return r.strip()
        return ''

    def split(self, st, ith, splim):
        '''
        split字符串,并获取第ith个
        :param st: str,字符串
        :param ith: str,获取第ith个字符串
        :param splim: 分隔符
        :return:
        '''
        sp = st.split(splim)
        if len(sp) >= ith+1:
            return sp[ith]
        else:
            return ''

    def getContent(self, html, rule):
        '''
        解析文章内容
        :param html:
        :param rule:
        :return:
        '''
        ps = html.xpath(rule)  # 段落
        psl = []  # 段落
        fj = []
        # print(ps)
        for p in ps:  # 提取每段html中的文字
            l = p.xpath('string(.)')
            l = l.strip()
            psl.append(l)
        return '\n'.join(psl)

    # def secXpath(self, elem, rule):
    #     '''
    #     安全的xpath
    #     :param elem:
    #     :param rule:
    #     :return:
    #     '''
    #     try:
    #         r = elem.xpath(rule)
    #     except:
    #         r = []
    #     return r

if __name__ == '__main__':
    t = CrawBase()
    url = 'http://www.ganzhou.gov.cn/c100080/list_zw_wj.shtml'
    print(t.get(url))