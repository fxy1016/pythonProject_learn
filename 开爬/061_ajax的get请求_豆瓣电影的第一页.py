# _*_ coding:utf-8 _*_
# @Time : 2022/9/28 23:06
# @Author : fx
# @File : 061_ajax的get请求_豆瓣电影的第一页
# @Project : pythonProject

import urllib.request
import json

url = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100:90&action=&start=0&limit=20'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
context = response.read().decode('utf-8')
# print(context)
fp = open('豆瓣情色.json', 'w', encoding='utf-8')
fp.write(context)
fp.close()





























