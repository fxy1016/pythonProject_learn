# _*_ coding:utf-8 _*_
# @Time : 2022/10/1 11:14
# @Author : fx
# @File : selenium_官方教程
# @Project : pythonProject

# 这个世界实在是太美了

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 导入驱动
service = Service(executable_path=ChromeDriverManager().install())
# 创建实例，类似
driver = webdriver.Chrome(service=service)
# 输入网址
driver.get('https://www.baidu.com')
# 获取title
title = driver.title
print(title)
# 创建等待策略
# driver.implicitly_wait(0.5)
baidu_input = driver.find_element(by=By.ID, value='kw')
baidu_button = driver.find_element(by=By.ID, value="su")
baidu_input.send_keys('田壮')
# driver.implicitly_wait(3)
baidu_button.click()

# driver.quit()
