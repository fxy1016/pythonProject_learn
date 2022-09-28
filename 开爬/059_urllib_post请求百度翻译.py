# _*_ coding:utf-8 _*_
# @Time : 2022/9/28 20:09
# @Author : fx
# @File : 059_urllib_post请求百度翻译
# @Project : pythonProject

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.0.0 Safari/537.36'
}
# post的请求必须编码
data = {
    'kw': 'happy'
}

new_data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=new_data, headers=headers)
# print(request)
response = urllib.request.urlopen(request)
context = response.read().decode('utf-8')
# print(context)

obj = json.loads(context)
print(obj)