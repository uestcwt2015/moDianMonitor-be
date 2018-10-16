# -*- coding: UTF-8 -*-

import re

def getIdFromURL(url):
    res = re.search('[0-9]+', url)
    return res.group()

def getMoneyFromText(text):
    pattern = re.compile(r'\d+')
    return ''.join(pattern.findall(text))