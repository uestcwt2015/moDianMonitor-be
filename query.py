# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import json

from utils.reg import getIdFromURL, getMoneyFromText, getHtmlFromRespones, getUidFromStr

configDict = {
    'name': '李梓',
    'url': 'https://zhongchou.modian.com/item/22903.html'
}

itemId = getIdFromURL(configDict['url'])

html = requests.get(configDict['url'])
html.encoding = 'utf-8'

def getPageInfo():
    bs = BeautifulSoup(html.text, 'lxml')
    project = bs.find('div', class_='project-goal')

    total = project.find('span', class_='goal-money')
    endtime = bs.find('div', class_='remain-time').find('h3')
    supporter = bs.find('div', class_='support-people').find('span')
    curr = project.select('h3')[0].select('span')[0]
    
    return {
        'total': getMoneyFromText(total.text),
        'curr': getMoneyFromText(curr.text),
        'endtime': endtime.attrs['end_time'],
        'supporter': supporter.text
    }

def getSuplist(pageNum):
    global itemId
    pageId = 1
    while (pageId <= pageNum):
        supurl = 'https://zhongchou.modian.com/realtime/ajax_dialog_user_list?jsonpcallback=jQuery1111042386962771442716_1540221823108&origin_id=%s&type=backer_list&page=%s&page_size=20' % (itemId, pageId)
        # print (supurl)
        res = requests.get(supurl)
        html = getHtmlFromRespones(res)
        getSupInfo(html)
        # break
        pageId += 1

def getSupInfo(text):
    bs = BeautifulSoup(text, 'lxml')
    items = bs.find_all('li')
    for item in items:
        dataHref = item.find('div', class_='item_logo').attrs["data-href"]
        conts = item.find('div', class_='item_cont').find_all('p')
        uid = getUidFromStr(dataHref)
        name = conts[0].text
        count = getMoneyFromText(conts[1].text)
        print (uid, name, count)
        # break

pageInfo = getPageInfo()
getSuplist(int(pageInfo["supporter"]) / 20 + 1)