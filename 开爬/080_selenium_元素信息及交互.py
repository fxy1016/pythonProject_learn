# _*_ coding:utf-8 _*_
# @Time : 2022/10/1 10:38
# @Author : fx
# @File : 080_selenium_元素信息及交互
# @Project : pythonProject

from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.baidu.com'
browser.get(url)

input = browser.find_element('id', 'su')
print(input.get_attribute('class'))
print(input.text)
