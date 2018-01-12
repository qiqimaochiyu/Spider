#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:41:49 2018

@author: macbook

抓取武汉的天气数据
python 3.6
url：http://www.weather.com.cn/weather1d/101200101.shtml#dingzhi_first
"""

import requests
import bs4

def get_html(url):
    '''
    封装请求
    '''
    headers = {
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Cookie':'vjuids=-38d158a85.160e54a3d3d.0.3c2db07c0d20e; vjlast=1515675336.1515675336.30; __asc=7964a800160e54a44d30f0c12b4; __auc=7964a800160e54a44d30f0c12b4; userNewsPort0=1; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1515675343; UM_distinctid=160e54a57cb257-0c30ccb6f18d2e-32677403-fa000-160e54a57cd1a9; CNZZDATA1262608253=1095204918-1515673244-null%7C1515673244; f_city=%E6%AD%A6%E6%B1%89%7C101200101%7C; defaultCity=101200101; Wa_lvt_1=1515675344; defaultCityName=%u6B66%u6C49; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1515675400; Wa_lpvt_1=1515675400',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'ContentType':'text/html; charset=utf-8',
            }
    
    try:
        htmlcontent = requests.get(url, headers=headers, timeout=30)
        htmlcontent.raise_for_status()
        htmlcontent.encoding = 'utf-8'
        return htmlcontent.text
    except:
        return '请求失败'


def get_content(url):
    '''
    抓取天气数据
    '''
    weather_list = []
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    content_ul = soup.find('div', class_='t').find_all('li')
    print(content_ul)
    for content in content_ul:
        try:
            weather = {}
            weather['day']=content.find('h1').text
            weather['temperature']=content.find('p', class_='tem').span.text + \
            content.find('p', class_='tem').em.text
            weather_list.append(weather)
        except:
            print('查不到')
    print(weather_list)

url='http://www.weather.com.cn/weather1d/101200101.shtml#dingzhi_first'
get_content(url)

