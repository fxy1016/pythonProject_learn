# _*_ coding:utf-8 _*_
# @Time : 2022/9/27 18:43
# @Author : fx
# @File : 047_文件的打开和关闭
# @Project : pythonProject

# 打开文件
f = open('../demo/text.txt', 'w')
# 写入
f.write('hello world')
# 文件关闭
f.close()