# _*_ coding:utf-8 _*_
# @Time : 2022/10/1 13:26
# @Author : fx
# @File : 087_requests_代理
# @Project : pythonProject
import requests

url = 'https://www.baidu.com/s?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.0.0 Safari/537.36'
}

data = {
    'wd': 'ip'
}
proxy = {
    'http': '183.247.202.208:30001'
}

response = requests.get(url=url, headers=headers, params=data, proxies=proxy)
response.encoding = 'utf-8'
content = response.text
with open('代理点_requests.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
