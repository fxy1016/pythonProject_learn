# _*_ coding:utf-8 _*_
# @Time : 2022/9/30 14:38
# @Author : fx
# @File : 073_urllib_jsonpath
# @Project : pythonProject
import jsonpath
import json

obj = json.load(open('073_urllib_jsonpath.json', 'r', encoding='utf-8'))
# print(obj)
author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(author_list)
