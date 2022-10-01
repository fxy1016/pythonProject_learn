# _*_ coding:utf-8 _*_
# @Time : 2022/10/1 12:57
# @Author : fx
# @File : 084_requests_基本使用
# @Project : pythonProject
import requests

url = 'https://www.baidu.com'
response = requests.get(url=url)
# 设置响应编码
response.encoding = 'utf-8'
# 返回网页源码
print(response.text)
# 返回url地址
print(response.url)
# 返回二进制数据
print(response.content)
# 返回响应的状态码
print(response.status_code)
# 返回响应头
print(response.headers)
