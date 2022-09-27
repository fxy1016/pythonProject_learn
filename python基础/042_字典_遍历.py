# _*_ coding:utf-8 _*_
# @Time : 2022/9/27 16:44
# @Author : fx
# @File : 042_字典_遍历
# @Project : pythonProject

person = {'name': 'fx', 'age': 18}
# 便利key
for key in person.keys():
    print(key)
# 便利value
for value in person.values():
    print(value)
# 便利字典中的key和value
for key, value in person.items():
    print(key, value)
# 便利字典中的项目元素
for item in person.items():
    print(item)