# -*- coding:utf-8 -*-

import urllib2
import re


#网络爬虫之丑事百科

class csbk():
    def __init__(self):
        #网址：
        self.url ='http://www.qiushibaike.com'
        #网页号码
        self.Index='/hot/page/1'
        #模拟浏览器
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        #提前加载开关
        self.enable = True
        #存储信息内容
        self.storiesLst=[]


    #获取网页内容
    def getpage(self):
        url = self.url + self.Index
        request = urllib2.Request(url,headers=self.headers)
        try:
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print u'网页链接错误原因：\n',e.reason

    #从网页中筛选出想要的内容
    def getpageItems(self):
        pagecode = self.getpage()
        if not pagecode:
            print u'网页加载失败！'

        #丑事百科-不含图片
        regx = re.compile(r'<div class="author clearfix">.*?alt="(.*?)">.*?<div class="content">\n<span>(.*?)</span>',
                          re.S)
        Items = re.findall(regx, pagecode)
        return Items

    #判断是否需要获取新的故事
    def newstories (self):
        if self.enable == True and len(self.storiesLst) <2:
            self.storiesLst.extend(self.getpageItems())
            return True
        return None

    #开始，判断输入并打印结果
    def start(self):
        self.storiesLst.extend(self.getpageItems())
        while True:
            input = raw_input(u"输入回车键看浏览笑话，退出按'Q':")
            if input == "Q":
                self.enable = False
                break
            elif len(self.storiesLst) >= 1:
                print len(self.storiesLst)
                tmp = self.storiesLst[0]
                self.storiesLst.pop(0)
                print tmp[0].strip()+':\n  '+tmp[1].strip()+'\n'
                self.newstories()
            else:
                print u"休息下再来看吧~"
                break
        return u"祝你快乐每一天!"


first = csbk()
print first.start()

