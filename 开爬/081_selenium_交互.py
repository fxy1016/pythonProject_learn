# _*_ coding:utf-8 _*_
# @Time : 2022/10/1 10:46
# @Author : fx
# @File : 081_selenium_交互
# @Project : pythonProject
from selenium import webdriver
import time

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.baidu.com'
browser.get(url)

time.sleep(2)

baidu_input = browser.find_element('id', 'kw')
baidu_input.send_keys('张伟')
time.sleep(3)

baidu_button = browser.find_element('id', 'su')
baidu_button.click()

# 不知为何，滑动不了底部
js_bottom = 'document.documentElement.scrollTop=10000'
browser.execute_script(js_bottom)
time.sleep(6)

baidu_next = browser.find_element('xpath', '//[@class="n"]')
baidu_next.click()
time.sleep(2)

browser.back()
browser.forward()

browser.quit()