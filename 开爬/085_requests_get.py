# _*_ coding:utf-8 _*_
# @Time : 2022/10/1 13:01
# @Author : fx
# @File : 085_reauests_get
# @Project : pythonProject
import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.0.0 Safari/537.36'
}

data = {
    'wd': '北京'
}

response = requests.get(url=url, headers=headers, data=data)
response.encoding='utf-8'
content = response.text
print(content)
