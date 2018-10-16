# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import json

from utils.reg import getIdFromURL, getMoneyFromText

configDict = {
    'name': '李梓',
    'url': 'https://zhongchou.modian.com/item/24271.html'
}

itemId = getIdFromURL(configDict['url'])

html = requests.get(configDict['url'])
html.encoding = 'utf-8'

def getPageInfo(html):
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

print(getPageInfo(html))
