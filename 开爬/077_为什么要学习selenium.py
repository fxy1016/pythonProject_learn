# _*_ coding:utf-8 _*_
# @Time : 2022/9/30 16:06
# @Author : fx
# @File : 077_为什么要学习selenium
# @Project : pythonProject
import urllib.request

url = 'https://www.jd.com/'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
print(content)
