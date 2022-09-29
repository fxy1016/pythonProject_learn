# _*_ coding:utf-8 _*_
# @Time : 2022/9/29 13:25
# @Author : fx
# @File : 067_urllib_代理
# @Project : pythonProject
import urllib.request

url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.0.0 Safari/537.36'
}

proxies = {
    'http': '202.109.157.65:9000'
}

request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)

handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')
with open('代理点.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
