# -*- coding:utf-8 -*-

import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class MovieCheck():

    def __init__(self):

        self.url = "https://piaofang.wepiao.com/"
        self.Moviename = u"战狼2"
        self.story = []

    def getValue(self):
        decodeName = self.Moviename.decode('utf-8')
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}

        try:
            request = urllib2.Request(self.url, headers=headers)
            response = urllib2.urlopen(request).read().decode('utf-8')
            with open('tmp.html','w+') as html:
                html.write(response)

            pattern = r'<td class="moviename-td" title="(.*?)"'
            print pattern
            regx = re.compile(pattern, re.S)
            data = re.findall(regx, response)
            print data
            #print data.group(1)
            #return data.group(1)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print e.reason
            if hasattr(e, 'code'):
                print e.code
    def Output(self):
        print self.Moviename
        print self.getValue()

langlang = MovieCheck()
langlang.Output()





