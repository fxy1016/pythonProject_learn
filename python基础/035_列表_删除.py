# _*_ coding:utf-8 _*_
# @Time : 2022/9/27 15:48
# @Author : fx
# @File : 035_列表_删除
# @Project : pythonProject

a = [1, 2, 3, 4, 5, 6]
print(a)
del a[5]
# 删除最后一个元素
a.pop()
a.remove(3)
print(a)
