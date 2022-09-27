# _*_ coding:utf-8 _*_
# @Time : 2022/9/27 18:49
# @Author : fx
# @File : 048_文件的读写
# @Project : pythonProject

# 文件会覆盖
# f = open("../demo/text.txt", 'w')
# f.write('hello fx\n' * 10)
# f.close()

# 读
f = open('../demo/text.txt', 'r')
# read一个个字节的读
# context = f.read()
# 一行一行的读，但只能读一行
# context = f.readline()
# 一行一行的读，可以读多行
context = f.readlines()
print(context)
