# -*- coding:utf-8 -*-


import urllib,re

def page(pgn):
    url='https://www.pengfu.com/index_%s.html'%pgn
    html = urllib.urlopen(url).read()
    return html

def title(html):
    reg=re.compile(r'<h1 class="dp-b"><a href=".*?" target="_blank">(.*?)</a></h1>')
    titles = re.findall(reg,html)
    return titles

def context():
    html = page(2)
    reg = re.compile(r'<div class="content-img clearfix pt10 relative">(.*?)</div>',re.S)
    contexts = re.findall(reg,html)
    return contexts

print len(context())

for i in context():
    print i

