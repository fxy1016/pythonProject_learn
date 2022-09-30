# _*_ coding:utf-8 _*_
# @Time : 2022/9/30 15:26
# @Author : fx
# @File : 075_urllib_bs4基本使用
# @Project : pythonProject
import lxml
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('075_urllib_bs4基本使用.html',encoding='utf-8'),'lxml')
# 获取第一个找到的标签
print(soup.a)
# 获取标签属性和属性值
print(soup.a.attrs)