# _*_ coding:utf-8 _*_
# @Time : 2022/9/30 15:53
# @Author : fx
# @File : 076_urllib_bs4_starbucks
# @Project : pythonProject
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'
response = urllib.request.urlopen(url=url)
content = response.read().decode('utf-8')

soup = BeautifulSoup(content,'lxml')
# //ul[@class="grid padded-3 product"]//strong/text()
name_list = soup.select('ul[class="grid padded-3 product"] strong')
# print(name_list)
for name in name_list:
    print(name.string)