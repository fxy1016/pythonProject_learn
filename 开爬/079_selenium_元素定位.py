# _*_ coding:utf-8 _*_
# @Time : 2022/10/1 10:27
# @Author : fx
# @File : 079_selenium_元素定位
# @Project : pythonProject

from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.baidu.com'
browser.get(url)

# 元素定位
# byid
# button = browser.find_element('id','su')
# by name
button = browser.find_element('name','wd')
print(button)