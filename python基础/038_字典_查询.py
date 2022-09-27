# _*_ coding:utf-8 _*_
# @Time : 2022/9/27 16:16
# @Author : fx
# @File : 038_字典_查询
# @Project : pythonProject

person = {'name': 'fx', 'age': 18}
print(person['name'])

# KeyError: 'sex'
# print(person['sex'])
# None
print(person.get('sex'))