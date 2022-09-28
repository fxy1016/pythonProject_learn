# _*_ coding:utf-8 _*_
# @Time : 2022/9/28 19:55
# @Author : fx
# @File : 058_urllib_get请求的urlencode方法
# @Project : pythonProject

# import urllib.parse
#
# data = {
#     'wd': '周杰伦',
#     'sex': '男'
# }
#
# a = urllib.parse.urlencode(data)
# print(a)

import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾'
}

new_data = urllib.parse.urlencode(data)

url = base_url + new_data
# print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
context = response.read().decode('utf8')
print(context)