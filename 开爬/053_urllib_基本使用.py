# _*_ coding:utf-8 _*_
# @Time : 2022/9/28 7:20
# @Author : fx
# @File : 053_urllib_基本使用
# @Project : pythonProject
import urllib.request
# 定义一个url
url = 'http://www.baidu.com'

# 模拟浏览器
response = urllib.request.urlopen(url)

# 获取源码
# 二进制->字符串
content = response.read().decode('utf-8')

# 打印数据
print(content)