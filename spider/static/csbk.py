# -*- coding:utf-8 -*-

import urllib2,re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def page(index):
    url = 'http://www.qiushibaike.com/hot/page/%s'%index
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    try:
        request = urllib2.Request(url,headers=headers)
        pg=urllib2.urlopen(request).read().decode('utf-8')

        return pg
    except urllib2.URLError,e:
        if hasattr(e,'code'):
            print e.code
        if hasattr(e,'reason'):
            print e.reason


def context(num):
    tmp = page(num)
    regx = re.compile(r'<div class="author clearfix">.*?alt="(.*?)">.*?<div class="content">\n<span>(.*?)</span>',re.S)

    items = re.findall(regx,tmp)
    return items



sub = context(1)
for i in range(len(sub)):
    name=sub[i][0]
    text=sub[i][1].strip()
    with open('tmp.txt','a') as file:
        nameandtext = '**************'+'\n'+name+':\n  '+text+'\n'
        file.write(nameandtext)
#    print "**************************"
#    print name,':\n  ',text



