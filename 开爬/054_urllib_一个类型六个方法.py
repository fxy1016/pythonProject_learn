# _*_ coding:utf-8 _*_
# @Time : 2022/9/28 7:27
# @Author : fx
# @File : 054_urllib_一个类型六个方法
# @Project : pythonProject

import urllib.request
# 定义一个url
url = 'http://www.baidu.com'
# 模拟浏览器
response = urllib.request.urlopen(url)
# <class 'http.client.HTTPResponse'>
# print(type(response))
# <class 'bytes'>
# context = response.read()
# print(type(context))
# 返回多少个字节
# context = response.read(5)

# context = response.readline()
# print(context)

# context = response.readlines()
# print(context)


# 获取状态码
# print(response.getcode())

print(response.geturl())
print(response.getheaders())








