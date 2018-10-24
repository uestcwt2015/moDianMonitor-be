# -*- coding: UTF-8 -*-

import re

def getIdFromURL(url):
    res = re.search('[0-9]+', url)
    return res.group()

def getMoneyFromText(text):
    pattern = re.compile(r'[0-9]+.[0-9]+')
    return ''.join(pattern.findall(text))

def getHtmlFromRespones(res):
    pattern = re.compile(r'<ul[\s\S]*<[\s\S]*>')
    resstr = res.text.encode('utf-8').decode('unicode_escape')

    content = re.sub(r'\\n', '', pattern.findall(resstr)[0])
    contentStr = re.sub(r'\\/', '/', content)
    
    return contentStr

def getUidFromStr(url):
    pattern = re.compile(r'[0-9]+')
    return pattern.findall(url)[0]


