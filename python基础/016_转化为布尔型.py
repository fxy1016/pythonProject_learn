# _*_ coding:utf-8 _*_
# @Time : 2022/9/26 21:02
# @Author : fx
# @File : 016_转化为布尔型
# @Project : pythonProject

# 整型--布尔,非零为True，0为False
a = 1
print(a)
print(type(a))
print(bool(a))
print(type(bool(a)))

# 浮点数--布尔,非零为True，0.0为False
a = 1.0
print(a)
print(type(a))
print(bool(a))
print(type(bool(a)))

# 字符串--布尔,有内容就为True
a = "love"
print(a)
print(type(a))
print(bool(a))
print(type(bool(a)))

# 列表--布尔,有内容就为True
a = ['I', 'Love', 'Your', 'Mom']
print(a)
print(type(a))
print(bool(a))
print(type(bool(a)))

# 元组--布尔,有内容就为True
a = ('I', 'Love', 'Your', 'Mom')
print(a)
print(type(a))
print(bool(a))
print(type(bool(a)))

# 字典--布尔,有内容就为True
a = {'I': 'me', 'Love': 'hate', 'Your': 'Yours', 'Mom': 'Father'}
print(a)
print(type(a))
print(bool(a))
print(type(bool(a)))
