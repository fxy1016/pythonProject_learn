# _*_ coding:utf-8 _*_
# @Time : 2022/9/29 13:58
# @Author : fx
# @File : 070_urllib_xpath基本使用
# @Project : pythonProject
from lxml import etree

tree = etree.parse('070_urllib_xpath基本使用.html')
# tree.xpath('xpath路径')

li_list = tree.xpath('//ul/li')
print(li_list)
print(len(li_list))