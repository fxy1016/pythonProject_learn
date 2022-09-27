# _*_ coding:utf-8 _*_
# @Time : 2022/9/27 18:58
# @Author : fx
# @File : 049_文件的序列化和反序列化
# @Project : pythonProject

import json

# dumps
# fp = open("../demo/text.txt", 'w')
# name_list = ['zhangSan', 'lisi']
# # 变为字符串
# # names = json.dumps(name_list)
# # fp.write(names)
#
# # 一步到位哦
# json.dump(name_list,fp)
# fp.close()

fp = open('../demo/text.txt', 'r')
# content = fp.read()
# print(content)
# print(type(content))

# loads load
# result = json.loads(content)
result = json.load(fp)
print(result)
print(type(result))
fp.close()
