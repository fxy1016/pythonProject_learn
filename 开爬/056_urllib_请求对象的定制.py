# _*_ coding:utf-8 _*_
# @Time : 2022/9/28 7:44
# @Author : fx
# @File : 056_urllib_请求对象的定制
# @Project : pythonProject
import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
context = response.read().decode('utf8')
print(context)
