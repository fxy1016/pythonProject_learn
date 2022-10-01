# _*_ coding:utf-8 _*_
# @Time : 2022/10/1 8:59
# @Author : fx
# @File : 078_selenium基本使用
# @Project : pythonProject

from selenium import webdriver

path = 'chromedriver.exe'
# DeprecationWarning: executable_path has been deprecated, please pass in a Service object
#   browser = webdriver.Chrome(path)
# 提示已经过时
browser = webdriver.Chrome(executable_path=path)
url = 'https://www.baidu.com'
browser.get(url)
content = browser.page_source
print(content)
