# _*_ coding:utf-8 _*_
# @Time : 2022/9/29 15:48
# @Author : fx
# @File : 071_urllib_百度一下获取
# @Project : pythonProject
import urllib.request
from lxml import etree

url = 'https://www.baidu.com'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 Safari/537.36'
    }

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

tree = etree.HTML(content)
result = tree.xpath('//input[@id="su"]/@value')
print(result)
